from rest_framework import generics,permissions
from library.models import Book
from library.serialisers import BookSerializer

# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    permissions = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer


class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    permissions = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
