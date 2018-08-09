from rest_framework import serializers
from classes.models import Classroom 

class listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'year', 'teacher',]