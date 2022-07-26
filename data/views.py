from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from data.models import Team, Group
from data.serializers import TeamSerializer, GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TeamViewSet(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
