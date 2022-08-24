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
    # 관리자 대시보드 페이지 url
    path("admin/", views.admin, name="admin"),
    # 작가 등록 신청 내역 조회 페이지 url
    path("admin/register/", views.admin_register, name="admin_register"),
    # 작가 통계 페이지 url
    path("admin/statistics/", views.admin_statistics, name="admin_statistics"),
]
