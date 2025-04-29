from django.urls import path
from . import views

urlpatterns = [
    path('',    views.main_view,          name='main'),
    path('game/',  views.new_game_view,       name='new_game'),
    path('players/', views.players_data_view, name='players_data'),
    path('league/', views.league_table, name='league_table'),
    path('league/play-round/', views.play_round, name='play_round'),
    path('league/reset/',   views.reset_league, name='reset_league'),
    path('api/matches/<match_id>/', views.match_detail_json),
]