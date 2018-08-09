from django.shortcuts import render
from rest_framework.generics import ListAPIView
from classes.models import Classroom
from ClassRoomsApp.Serializer import listSerializer 

# Create your views here.

class ListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = listSerializer

