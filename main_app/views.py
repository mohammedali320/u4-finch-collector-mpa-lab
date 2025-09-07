from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Bird:
    def __init__(self, name, species, description, age):
        self.name = name
        self.species = species
        self.description = description
        self.age = age


birds = [
    Bird('Tweety', 'Canary', 'Yellow and chirpy.', 1),
    Bird('Koko', 'Parrot', 'Loves to mimic sounds.', 4),
    Bird('Hoot', 'Owl', 'Quiet at day, active at night.', 3),
    Bird('Sky', 'Blue Jay', 'Bright blue feathers.', 2)
]
# views.py

def bird_index(request):
    return render(request, 'birds/index.html', {'birds': birds})