from django.shortcuts import render

from web.forms import UserLoginForm


def index(request):
    # Create your views here.
    form = UserLoginForm(request.POST or None)
    title = "Login"
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

    return render(request, "web/index.html", {"form": form, "title": title})


