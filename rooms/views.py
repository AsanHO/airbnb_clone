from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    model = models.Room


def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})


"""

def all_rooms(request):  # 함수명 마음대로
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(
        room_list, 10, orphans=5
    )  # orphan=5 고아가 5개이하면 이전 페이지에 종속, 5개를 넘어가면 다음페이지 생성
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", {"rooms": rooms})
"""
"""def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect("/")"""
