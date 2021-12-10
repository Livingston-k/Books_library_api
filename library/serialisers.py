from rest_framework import serializers
from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "title",
            "color",
            "publish_date",
            "price",
            "num_pages",
            "isbn13"]
        extra_kwags = {
            "publish_date": {"requred": False},
            "color": {"requred": False},
            "price": {"requred": False},
            "isbn13": {"requred": False},
        }
