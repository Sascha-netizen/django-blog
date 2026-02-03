from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    about_entry = About.objects.first()
    context = { "about": about_entry }

    return render(
        request,
        "about/about.html",
        context,
    )