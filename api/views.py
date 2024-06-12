from django.shortcuts import render
from django.http import JsonResponse, response
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *

import requests

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
    serializer_class = GameSerializer

class RecentlyReleasedGameView(generics.ListAPIView):

    today = date.today()
    queryset = Game.objects.all().filter(release_date__lte = today).order_by('-release_date')
    serializer_class = GameSerializer

class ComingSoonGameView(generics.ListAPIView):

    tomorrow = date.today() + timedelta(1)
    queryset = Game.objects.all().filter(release_date__gte = tomorrow).order_by('release_date')
    serializer_class = GameSerializer
        
class SteamReviewsView(generics.RetrieveAPIView):

    def get(self, request, steamappid, *args, **kwargs):
        try:
            # URL of the external server's API endpoint
            external_api_url = 'https://store.steampowered.com/appreviews/'+str(steamappid)+'?json=1&purchase_type=all'
            
            # Make a GET request to the external API
            response = requests.get(external_api_url)
            
            # Raise an exception if the request was unsuccessful
            response.raise_for_status()
            
            # Get the data from the response
            data = response.json()
            
            # Return the data as a JSON response
            return Response(data, status=status.HTTP_200_OK)
        except requests.RequestException as e:
            # Handle errors in making the external request
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class SteamGameView(generics.ListAPIView):
    
    queryset = Game.objects.exclude(steam = "").order_by('?')
    serializer_class = GameSerializer

class EpicGameView(generics.ListAPIView):
    
    queryset = Game.objects.exclude(epic = "").order_by('?')
    serializer_class = GameSerializer

class GoGGameView(generics.ListAPIView):
    
    queryset = Game.objects.exclude(gog = "").order_by('?')
    serializer_class = GameSerializer

class PlaystationGameView(generics.ListAPIView):
    
    queryset = Game.objects.exclude(playstation = "").order_by('?')
    serializer_class = GameSerializer

class XboxGameView(generics.ListAPIView):
    
    queryset = Game.objects.exclude(xbox = "").order_by('?')
    serializer_class = GameSerializer

class SwitchGameView(generics.ListAPIView):
    
    queryset = Game.objects.exclude(nintendo = "").order_by('?')
    serializer_class = GameSerializer