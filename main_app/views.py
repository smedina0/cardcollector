from django.shortcuts import render
from django.http import HttpResponse
from .models import Card

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


def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})

# NOTE: url params are explicitly passed to view functions seperate from the request object


def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'cards/detail.html', {'card': card})
