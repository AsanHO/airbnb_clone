from django.urls import path
from rooms import views as room_views

app_name = "core"  # config urlpatterns의 namespace와 이름의 app_name 변수 선언이 있어야함

urlpatterns = [path("", room_views.all_rooms, name="home")]
