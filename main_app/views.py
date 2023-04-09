from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Card
from .forms import CleaningForm

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

class CardList(ListView):
    model = Card
    context_object_name = 'cards'
    template_name = 'cards/card_index.html'


class CardDetail(DetailView):
    model = Card
    context_object_name = 'card'
    cleaning_form = CleaningForm()
    template_name = 'cards/card_detail.html'
    pk_url_kwarg = 'card_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cleaning_form'] = CleaningForm()
        return context


def add_cleaning(request, card_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.card_id = card_id
        new_cleaning.save()
    return redirect('card_detail', card_id=card_id)


class CardCreate(CreateView):
    model = Card
    fields = '__all__'
    # success_url = '/cards/'
    template_name = 'cards/card_form.html'


class CardUpdate(UpdateView):
    model = Card
    fields = ['name', 'game', 'condition', 'value']
    template_name = 'cards/card_form.html'


class CardDelete(DeleteView):
    model = Card
    success_url = '/cards/'
    template_name = 'cards/card_confirm_delete.html'
