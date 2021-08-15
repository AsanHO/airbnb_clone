from math import ceil
from django.shortcuts import render
from . import models


def all_rooms(request):  # 함수명 마음대로
    page = int(
        request.GET.get("page", 1)
    )  # http://127.0.0.1:8000/?page=2 의 페이지 숫자로 url 구성
    page = int(page or 1)  # page = == page = 1 과 동일하게 만들어준다.
    page_size = 10  # 한페이지에 들어가는 room의 갯수
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]  # 변수명도 마음대로 #[시작값:리미트]
    page_count = ceil(
        models.Room.objects.count() / page_size
    )  # 페이지 개수 = (모든 방의 갯수/페이지사이즈)
    return render(
        request,
        "rooms/home.html",
        {
            "potato": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )  # {이 딕션에 있는 변수만이 템플릿에서 호출할 수 있다.}
