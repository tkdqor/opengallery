from django.urls import path

from . import views

app_name = "writers"

urlpatterns = [
    # 작가 목록 조회 페이지 url
    path("", views.list, name="list"),
    # 작품 목록 조회 페이지 url
    path("painting/", views.painting, name="painting"),
]
