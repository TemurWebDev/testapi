from django.shortcuts import render
from api.models import Books

# Create your views here.

def webbook(requests):
    book = Books.objects.all()

    return render(requests,'book.html',{'book':book})


