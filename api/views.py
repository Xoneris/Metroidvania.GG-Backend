from django.shortcuts import render
from django.http import JsonResponse, response
from django.db.models import Q

from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *

from datetime import date, timedelta

# Create your views here.
class GameView(generics.ListAPIView):

    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer

class SingleGameView(generics.RetrieveAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "slug"

class DemoGameView(generics.ListAPIView):
    
    queryset = Game.objects.filter(demo = True).order_by('?')
    serializer_class = GameSerializer

class EarlyAccessGameView(generics.ListAPIView):
    
    queryset = Game.objects.filter(earlyaccess = True).order_by('?')
    serializer_class = GameSerializer

class UpcomingKickstarterGameView(generics.ListAPIView):

    queryset = Game.objects.filter(kickstarter_status = 'Upcoming').order_by('?')
    serializer_class = GameSerializer

class LiveKickstarterGameView(generics.ListAPIView):

    queryset = Game.objects.filter(kickstarter_status = 'Live').order_by('?')
    serializer_class = GameSerializer

class ReleaseIn2024GameView(generics.ListAPIView):
    tomorrow = date.today() + timedelta(1)
    queryset = Game.objects.filter(Q(release_window__contains = '2024') | Q(release_date__range = [tomorrow, '2024-12-31'])).order_by('?')
    serializer_class = GameSerializer

class ReleaseIn2025GameView(generics.ListAPIView):
    
    queryset = Game.objects.filter(Q(release_window__contains = '2025') | Q(release_date__range = ['2025-01-01', '2025-12-31'])).order_by('?')
    serializer_class = GameSerializer

class ReleaseIn2026GameView(generics.ListAPIView):

    queryset = Game.objects.filter(Q(release_window__contains = '2026') | Q(release_date__range = ['2026-12-31', '2026-12-31'])).order_by('?')
    serializer_class = GameSerializer

class TBDGameView(generics.ListAPIView):
    queryset = Game.objects.filter(release_window = 'TBD').order_by('?')
    serializer_class = GameSerializer

class HeroGameView(generics.ListAPIView):

    today = date.today()
    tomorrow = date.today() + timedelta(1)

    kickstarter_qs = Game.objects.all().filter(kickstarter_status = "Live")
    last_release_qs = Game.objects.all().filter(release_date__lte = today).order_by('-release_date')
    next_upcoming_qs = Game.objects.all().filter(release_date__gte = tomorrow).order_by('release_date')
    early_access_qs = Game.objects.all().filter(earlyaccess = True).order_by('?')

    queryset = kickstarter_qs.union(last_release_qs, next_upcoming_qs, early_access_qs)

    # queryset = Game.objects.all().filter(kickstarter_status = "Live")
    # q2 = Game.objects.all().filter(release_date__lte = today)
    # q3 = Game.objects.all().filter(release_date__gte = tomorrow)
    # q4 = Game.objects.all().filter(earlyaccess = True).order_by('?')

    # def get_queryset(self):
    #     today = date.today()
    #     tomorrow = date.today() + timedelta(1)


    #     kickstarter_qs = Game.objects.all().filter(kickstarter_status = "Live")
    #     last_release_qs = Game.objects.all().filter(release_date__lte = today).order_by('-release_date')
    #     next_upcoming_qs = Game.objects.all().filter(release_date__gte = tomorrow).order_by('release_date')
    #     early_access_qs = Game.objects.all().filter(earlyaccess = True).order_by('?')

    #     return kickstarter_qs.union(last_release_qs, next_upcoming_qs, early_access_qs)

    # queryset = Game.objects.filter(
    #     kickstarter_status = "Live").filter(
    #     release_date__lte = today).order_by('-release_date').filter(
    #     release_date__gte = tomorrow).order_by('release_date').filter(
    #     earlyaccess = True).order_by('?')


    serializer_class = GameSerializer

    

class RecentlyReleasedGameView(generics.ListAPIView):

    today = date.today()
    queryset = Game.objects.all().filter(release_date__lte = today).order_by('-release_date')
    serializer_class = GameSerializer

class ComingSoonGameView(generics.ListAPIView):

    tomorrow = date.today() + timedelta(1)
    queryset = Game.objects.all().filter(release_date__gte = tomorrow).order_by('release_date')
    serializer_class = GameSerializer


    