import re
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.shortcuts import redirect
from django.views.generic import ListView

print("http://127.0.0.1:5000/hello/VSCode")

# Create your views here.


# def home(request):
#     return render(request, "hello/home.html")


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def hello_there(request, name):
    return render(
        request, "hello/hello_there.html", {"name": name, "date": datetime.now()}
    )


def about(request):
    return render(request, "hello/about.html")


def contact(request):
    return render(request, "hello/contact.html")


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
