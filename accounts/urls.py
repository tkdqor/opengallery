from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    # 로그인/회원가입 페이지 url
    path("", views.accounts, name="index"),
    # 회원가입 url
    path("sign_up/", views.sign_up, name="sign_up"),
    # 로그인 url
    path("login/", views.login, name="login"),
    # 작가 페이지에서 대시보드 페이지 url
    path("my_writer/", views.my_writer, name="my_writer"),
    # 작품 등록 페이지 url
    path("my_writer/painting/", views.my_writer_painting, name="my_writer_painting"),
    # 전시 등록 페이지 url
    path("my_writer/exhibition/", views.my_writer_exhibition, name="my_writer_exhibition"),
]
