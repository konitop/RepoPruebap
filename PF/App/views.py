from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from App.models import Viewer, Streamer, Video
from App.forms import ViewerForm, StreamerForm, VideoForm
# Create your views here.

def inicio(request):
    return render(request, "App/inicio.html")
def videos(request):
    return render(request, "App/videos.html")
def registro(request):
     return render(request, "App/Registro.html")
def streamers(request):
     streamers= Streamer.objects.all()
     return render(request, "App/Streamers.html", {'streamers':streamers})

def basurita(request):
      return render(request, "App/basurita.html")


def viewerForm(request):
      if request.method == "POST":
            miForm = ViewerForm(request.POST, request.FILES)
            print(miForm)

            if miForm.is_valid():
                  info = miForm.cleaned_data
                  img = info.get('img')
                  viewer = Viewer(
                       realname=str(info['realname']),
                       surname=str(info['surname']),
                       mail=info['mail'],
                       img=img,
                  )
                  viewer.save()
                  return render(request, "App/inicio.html")
      else:
            miForm = ViewerForm()
 
      return render(request, "App/viewerForm.html", {"miForm": miForm})


def streamerForm(request):
      if request.method == "POST":
            miForm = StreamerForm(request.POST, request.FILES)
            print(miForm)

            if miForm.is_valid():
                  info = miForm.cleaned_data
                  img = info.get('img')
                  streamer = Streamer(
                        username=str(info['username']),
                        mail=info['mail'],
                        desc=str(info['desc']),
                        link=str(info['link']),
                        img=img,
                  )

                  streamer.save()
                  return render(request, "App/inicio.html")
      else:
            miForm = StreamerForm()
 
      return render(request, "App/streamerForm.html", {"miForm": miForm})


def videoForm(request):
      if request.method == "POST":
            miForm = VideoForm(request.POST) # Aqui me llega la informacion del html
            print(miForm)

            if miForm.is_valid():
                  info = miForm.cleaned_data
                  video = Video(
                       title= str(info['title']),
                       mins= int(info['mins']),
                       sec= int(info['sec']),
                       date=info['date'],
                       author= str(info['author']),
                       link= str(info['link']),
                       gif= str(info['gif']),
                       )
                  
                  video.save()
                  return render(request, "App/inicio.html")
      else:
            miForm = VideoForm()
 
      return render(request, "App/videoForm.html", {"miForm": miForm})


