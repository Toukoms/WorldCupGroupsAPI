from rest_framework import routers

from data.views import GroupViewSet, TeamViewSet

routeur = routers.DefaultRouter()
routeur.register('groups', GroupViewSet)
routeur.register('teams', TeamViewSet)