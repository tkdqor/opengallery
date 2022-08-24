from django.urls import path

from . import views

app_name = "writers"

urlpatterns = [
    # 작가 목록 조회 페이지 url
    path("", views.list, name="list"),
    # 작품 목록 조회 페이지 url
    path("painting/", views.painting, name="painting"),
    # 작가 등록 신청 페이지 url
    path("register/", views.register, name="register"),
]
