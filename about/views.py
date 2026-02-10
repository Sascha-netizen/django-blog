from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages 


def about(request):
    about_entry = About.objects.first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )
            # reset form after successful submission
            collaborate_form = CollaborateForm()
    else:
        # For GET requests, show a blank form
        collaborate_form = CollaborateForm()

    context = { 
        "about": about_entry,
        "collaborate_form": collaborate_form,
    }

    return render(request, "about/about.html", context)
