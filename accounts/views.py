from django.contrib import auth
from django.shortcuts import redirect, render

from accounts.models import User


# url : GET accounts/
def accounts(request):
    """
    Assignee : 상백

    로그인 또는 회원가입을 진행할 수 있는 페이지
    """

    return render(request, "accounts/index.html")


# url : GET,POST accounts/sign_up/
def sign_up(request):
    """
    Assignee : 상백

    GET : 회원가입을 진행할 수 있는 페이지 구현
    회원가입 시, html type를 이용해서 이메일과 전화번호, 생년월일 형식 지정
    ex) aaa@naver.com, 010-6223-8078, 1995-01-17
    POST : 회원가입 진행 로직 구현, 회원가입 완료 시 로그인 진행
    """

    context = {}

    if request.method == "POST":
        if (
            request.POST.get("email")
            and request.POST.get("password")
            and request.POST.get("password") == request.POST.get("password_check")
        ):

            new_user = User.objects.create_user(
                email=request.POST.get("email"),
                password=request.POST.get("password"),
            )
            auth.login(request, new_user)

            user = User.objects.get(email=request.user.email)
            user.username = request.POST.get("username")
            user.gender = request.POST.get("gender")
            user.mobile = request.POST.get("mobile")
            user.birth = request.POST.get("birth")
            user.save()

            return redirect("accounts:index")
        else:
            context["error"] = "회원가입 입력사항을 다시 확인해주세요!"

    return render(request, "accounts/sign_up.html", context)


# url : POST accounts/login/
def login(request):
    """
    Assignee : 상백

    가입한 이메일 및 비밀번호로 로그인할 수 있도록 로직 구성
    auth로 인증이 되면 로그인 실행
    """

    context = {}

    if request.method == "POST":
        if request.POST.get("email") and request.POST.get("password"):
            print(request.POST.get("email"))
            print(request.POST.get("password"))
            user = auth.authenticate(request, email=request.POST.get("email"), password=request.POST.get("password"))

            if user is not None:
                auth.login(request, user)
                return redirect("accounts:index")
            else:
                context["error"] = "이메일과 비밀번호를 다시 입력해주세요!"
        else:
            context["error"] = "이메일과 비밀번호를 모두 입력해주세요!"
    return render(request, "accounts/index.html", context)
