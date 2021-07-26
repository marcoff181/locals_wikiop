from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from .serializers import FixedSectionSerializer, ProjectExampleSerializer, QuestionAndAnswerSerializer, PrimarySectionSerializer, SecondarySectionSerializer
from .models import FixedSection, PrimarySection, QuestionAndAnswer, ProjectExample, SecondarySection

class ProjectExampleViewSet(viewsets.ModelViewSet):
    queryset = ProjectExample.objects.all()
    serializer_class = ProjectExampleSerializer

class QuestionAndAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAndAnswer.objects.all()
    serializer_class = QuestionAndAnswerSerializer

class PrimarySectionViewSet(viewsets.ModelViewSet):
    queryset = PrimarySection.objects.all()
    serializer_class = PrimarySectionSerializer

class SecondarySectionViewSet(viewsets.ModelViewSet):
    queryset = SecondarySection.objects.all()
    serializer_class = SecondarySectionSerializer

class FixedSectionViewSet(viewsets.ModelViewSet):
    queryset = FixedSection.objects.all()
    serializer_class = FixedSectionSerializer
