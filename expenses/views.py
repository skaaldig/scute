from django.shortcuts import render
from django.forms.models import inlineformset_factory


def create_expense(request):
    return render(request, "build/index.html")