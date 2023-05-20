from django.urls import path
from App import views

urlpatterns= [
    path("", views.inicio, name="Inicio"),
    path("Videos", views.videos, name="Videos"),
    path("Registro", views.registro, name= "Registro"),
    path ("Streamers", views.streamers, name= "Streamers"),
    path('viewerForm', views.viewerForm, name="viewerForm"),
    path('streamerForm', views.streamerForm, name="streamerForm"),
    path('videoForm', views.videoForm, name="videoForm"),
    path('basurita', views.basurita, name="basurita"),
]