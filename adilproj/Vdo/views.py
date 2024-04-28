from django.shortcuts import render
from pytube import YouTube

# Create your views here.

def home(request):
    if request.method=="POST":
        link = request.POST.get('link')
        youtube_2 = YouTube(link)
        video = youtube_2.streams.get_highest_resolution()
        video.download()
        print(youtube_2.title)
        return render(request, "index.html")
    else:
        print("link has some typing errors!")
        return render(request, "index.html")

# link = "https://www.youtube.com/watch?v=-oo5SZyu36I"

