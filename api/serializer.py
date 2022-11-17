from rest_framework import serializers
from .models import Books

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['name','title','author','isbn']