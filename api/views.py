from rest_framework.generics import ListAPIView
from .serializer import BooksSerializers
from .models import Books

# Create your views here.

class BooksApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
