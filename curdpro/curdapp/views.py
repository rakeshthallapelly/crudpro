from django.shortcuts import render
from curdapp.models import Patient
from curdapp.serializers import PatientSerializer
from rest_framework import generics


class Create(generics.ListCreateAPIView):
	queryset=Patient.objects.all()
	serializer_class=PatientSerializer
class Retrive(generics.RetrieveUpdateDestroyAPIView):
	queryset=Patient.objects.all()
	serializer_class=PatientSerializer
