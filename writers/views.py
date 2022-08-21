from django.shortcuts import render

from .models import Painting, Writer


# url : GET writers/
def list(request):
    """
    Assignee : 상백

    작가 목록을 조회할 수 있는 페이지 구현
    최근에 등록된 순서대로 조회할 수 있게 ORM 메소드인 order_by를 created_at 내림차순으로 설정
    작가 이름, 성별, 생년월일, 연락처 정보 응답
    """

    writers = Writer.objects.all().order_by("-created_at")

    context = {
        "writers": writers,
    }

    return render(request, "writers/list.html", context)


# url : GET writers/painting/
def painting(request):
    """
    Assignee : 상백

    작품 목록을 조회할 수 있는 페이지 구현
    최근에 등록된 순서대로 조회할 수 있게 ORM 메소드인 order_by를 created_at 내림차순으로 설정
    작품 제목, 가격, 호수, 작가 정보 응답
    """

    paintings = Painting.objects.all().order_by("-created_at")

    context = {
        "paintings": paintings,
    }

    return render(request, "writers/painting.html", context)
