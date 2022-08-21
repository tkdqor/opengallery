from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    # 로그인/회원가입 페이지
    path("", views.accounts, name="index"),
    # 회원가입 url
    path("sign_up/", views.sign_up, name="sign_up"),
    # 로그인 url
    path("login/", views.login, name="login"),
]
