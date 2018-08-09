from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView,RetrieveUpdateAPIView,CreateAPIView
from classes.models import Classroom
from ClassRoomsApp.Serializer import listSerializer , deetailSerializer,createUpdateSerializer, createSerializer

# Create your views here.

class ListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = listSerializer


class Detailview(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = deetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class CreateView(CreateAPIView):
    serializer_class = createSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = createUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class DeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = listSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'