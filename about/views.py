from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ApproachForm


def about_me(request):

    if request.method == "POST":
        approach_form = ApproachForm(data=request.POST)
        if approach_form.is_valid():
            approach_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your message has been received! Kel will respond as early as possible.",
            )

    about = About.objects.all().order_by("-updated_on").first()
    approach_form = ApproachForm()
    return render(
        request,
        "about/about.html",
        {"about": about, "approach_form": approach_form},
    )
