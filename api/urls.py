from django.urls import path, include
from . import views

urlpatterns = [
    path('games/', views.GameView.as_view()),
    path('games/<slug:slug>', views.SingleGameView.as_view()),
    path('games/demo/', views.DemoGameView.as_view()),
    path('games/earlyaccess/', views.EarlyAccessGameView.as_view()),
    path('games/hero/', views.HeroGameView.as_view()),
    path('games/recentlyreleased/', views.RecentlyReleasedGameView.as_view()),
    path('games/comingsoon/', views.ComingSoonGameView.as_view()),
    path('games/kickstarter/upcoming/', views.UpcomingKickstarterGameView.as_view()),
    path('games/kickstarter/live/', views.LiveKickstarterGameView.as_view()),
    path('games/TBD/', views.TBDGameView.as_view()),
    path('games/2024/', views.ReleaseIn2024GameView.as_view()),
    path('games/2025/', views.ReleaseIn2025GameView.as_view()),
    path('games/2026/', views.ReleaseIn2026GameView.as_view()),
]