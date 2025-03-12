from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My CRUD API</h1>")

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
