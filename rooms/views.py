from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from . import models

# Create your views here.

# get의 2dn arg는 디폴트값 선정
def all_rooms(request):
    page = request.GET.get("page", 1)
    # 쿼리셋 is lazy : 쿼리셋은 호출 전까지 명령을 수행하지 않음, 생성시에 작동 x
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    # 11.5: get_page = exception시 마지막페이지, page=exception시 에러
    try:
        page = paginator.page(page)
        return render(request, "rooms/home.html", context={"page": page,},)
    # 11.6 모든 예외를 처리하려면 except Exception 으로 선언
    except EmptyPage:
        page = paginator.page(1)
        return redirect("/")
    print(vars(page.paginator))
    # 10.3 컨픽URL == 뷰 함수, 템플레이트명 == 뷰 리턴 템플레이트, html context명 == 뷰 리턴 context명
