from rest_framework import serializers
from classes.models import Classroom 
from django.contrib.auth.models import User

class listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'year', 'teacher',]

class deetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = '__all__'

class createSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = [
            'name',
            'subject',
            'year',
            ]


class createUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [
            'name',
            'subject',
            'year',
            'teacher',
            ]