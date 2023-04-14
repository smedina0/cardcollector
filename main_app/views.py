from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Card, Vendor, Photo
from .forms import CleaningForm
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3


S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'cardcollector'

# Create your views here.


# class Card:
#     def __init__(self, name, game, condition, value=0):
#         self.name = name
#         self.game = game
#         self.condition = condition
#         self.value = value


# cards = [
#     Card('Dark Magician', 'Yu-Gi-Oh', 'NM', 100),
#     Card('Blue-Eyes White Dragon', 'Yu-Gi-Oh', 'NM', 200),
#     Card('Exodia', 'Yu-Gi-Oh', 'NM', 50),
#     Card('Pikachu', 'Pokemon', 'NM', 100),
#     Card('Charizard', 'Pokemon', 'NM', 200),
#     Card('magic card', 'Magic', 'NM', 50),
#     Card('Baronne de fleur', 'Yu-Gi-Oh', 'NM', 100),
# ]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# def cards_index(request):
#     cards = Card.objects.all()
#     return render(request, 'cards/index.html', {'cards': cards})

# # NOTE: url params are explicitly passed to view functions seperate from the request object


# def cards_detail(request, card_id):
#     card = Card.objects.get(id=card_id)
#     return render(request, 'cards/detail.html', {'card': card})

class VendorList(LoginRequiredMixin, ListView):
    model = Vendor
    context_object_name = 'cards'
    template_name = 'vendors/index.html'


class VendorDetail(LoginRequiredMixin, DetailView):
    model = Vendor
    context_object_name = 'vendor'
    template_name = 'vendors/detail.html'
    pk_url_kwarg = 'vendor_id'


class VendorCreate(LoginRequiredMixin, CreateView):
    model = Vendor
    fields = '__all__'
    template_name = 'vendors/form.html'


class VendorUpdate(LoginRequiredMixin, UpdateView):
    model = Vendor
    fields = '__all__'
    template_name = 'vendors/form.html'


class VendorDelete(LoginRequiredMixin, DeleteView):
    model = Vendor
    success_url = '/vendors/'
    template_name = 'vendors/confirm_delete.html'


class CardList(LoginRequiredMixin, ListView):
    model = Card
    context_object_name = 'cards'
    template_name = 'cards/card_index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class CardDetail(LoginRequiredMixin, DetailView):
    model = Card
    context_object_name = 'card'
    cleaning_form = CleaningForm()
    template_name = 'cards/card_detail.html'
    pk_url_kwarg = 'card_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        card = self.get_object()
        card_vendor_ids = card.vendors.all().values_list('id')
        vendors_that_dont_have_card = Vendor.objects.exclude(
            id__in=card_vendor_ids)
        context['cleaning_form'] = CleaningForm()
        context['card_vendor_ids'] = card_vendor_ids
        context['vendors_that_dont_have_card'] = vendors_that_dont_have_card
        return context


@login_required
def assoc_vendor(request, card_id, vendor_id):
    card = Card.objects.get(id=card_id)
    card.vendors.add(vendor_id)
    return redirect('card_detail', card_id=card_id)


@login_required
def unassoc_vendor(request, card_id, vendor_id):
    card = Card.objects.get(id=card_id)
    card.vendors.remove(vendor_id)
    return redirect('card_detail', card_id=card_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('card_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})


def add_photo(request, card_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, card_id=card_id)
        except Exception as error:
            print('photo upload failed')
            print(error)
    return redirect('card_detail', card_id=card_id)


@login_required
def add_cleaning(request, card_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.card_id = card_id
        new_cleaning.save()
    return redirect('card_detail', card_id=card_id)


class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = ('name', 'game', 'condition', 'value')
    # success_url = '/cards/'
    template_name = 'cards/card_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CardUpdate(LoginRequiredMixin, UpdateView):
    model = Card
    fields = ['name', 'game', 'condition', 'value']
    template_name = 'cards/card_form.html'


class CardDelete(LoginRequiredMixin, DeleteView):
    model = Card
    success_url = '/cards/'
    template_name = 'cards/card_confirm_delete.html'
