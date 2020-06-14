from django.urls import path
from rooms import views as room_views

app_name = "core"

# path 의 arg는 URL과 function만 가능하다
urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"),
]
