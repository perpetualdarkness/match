from django.shortcuts import render, redirect
from .forms import MatchForm
from django.contrib import messages
# Create your views here.
def home(request):
    form = MatchForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Matched')
        return redirect('home')
    context = {
        "form": form,
        "title": "Match",
    }
    return render(request, "entry.html", context)
