
from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    #10.3 컨픽URL == 뷰 함수, 템플레이트명 == 뷰 리턴 템플레이트, html context명 == 뷰 리턴 context명
    return render(request, "rooms/home.html", context={"all_rooms":all_rooms
    })
