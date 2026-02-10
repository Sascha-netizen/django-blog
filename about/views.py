from django.shortcuts import render
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about(request):
    about_entry = About.objects.first()
    collaborate_form = CollaborateForm()
    context = { "about": about_entry, "collaborate": collaborate_form, }

    return render(
        request,
        "about/about.html",
        context,
    )