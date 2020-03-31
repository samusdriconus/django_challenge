from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .serializers import *



class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for view and edit students
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint for view and edit students
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]

