from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('photos/', views.photos, name='photos'),
    path('game/', views.game, name='game'),
    path('qa/', views.qa, name='qa'),
    path('letter/', views.letter, name='letter'),
]
