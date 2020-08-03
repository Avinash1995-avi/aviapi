from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BBTSerializer
from .models import BigBangTheory

class BBTView(viewsets.ModelViewSet):
    queryset = BigBangTheory.objects.all()
    serializer_class = BBTSerializer
# Create your views here.
