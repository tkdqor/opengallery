from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import User
from writers.models import Exhibition, Painting


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


# url : GET accounts/my_writer/
@login_required
def my_writer(request):
    """
    Assignee : 상백

    작가로 등록된 계정만 페이지를 조회할 수 있도록 if문 설정
    작가인 본인의 정보를 확인하고 등록된 작품과 전시를 확인 가능
    작품 및 전시 등록 버튼 설정
    """

    if request.user.writer.approval == True:
        user = request.user
        writer = user.writer

        context = {
            "writer": writer,
        }

        return render(request, "accounts/my_writer.html", context)
    else:
        return redirect("writers:list")


# url : GET,POST accounts/my_writer/painting/
def my_writer_painting(request):
    """
    Assignee : 상백

    GET : 작품 등록 페이지 구현
    html type을 이용해 제목 64자 이하 / 가격 0 이상 숫자 / 호수 1 이상 500 이하 숫자 설정
    POST : 작품 등록 로직 구현
    위의 정보 중 하나라도 없을 경우, context 딕셔너리로 에러 메시지 응답
    입력된 정보로 Painting 모델 객체 생성
    """

    context = {}

    if request.method == "POST":
        if request.POST.get("title") and request.POST.get("price") and request.POST.get("size"):
            title = request.POST.get("title")
            price = request.POST.get("price")
            size = request.POST.get("size")
            painting = Painting(title=title, price=price, size=size, writer=request.user.writer)
            painting.save()
            return redirect("accounts:my_writer")
        else:
            context["error"] = "등록 입력사항을 다시 확인해주세요!"
            return render(request, "accounts/my_writer_painting.html", context)
    else:
        return render(request, "accounts/my_writer_painting.html")


# url : GET,POST accounts/my_writer/exhibition/
def my_writer_exhibition(request):
    """
    Assignee : 상백

    GET : 전시 등록 페이지 구현
    html type을 이용해 제목 64자 이하 / 시작일과 종료일 캘린더 설정 / 작품 목록 선택 가능하게 설정
    작품 선택의 경우, Painting 모델과 Exhibition 모델을 1:1 관계로 설정해서 하나의 작품에 대한 전시를 진행한다고 생각
    POST : 전시 등록 로직 구현
    위의 정보 중 하나라도 없을 경우, context 딕셔너리로 에러 메시지 응답
    입력된 정보로 exhibition 모델 객체 생성
    """

    context = {}

    if request.method == "POST":
        if (
            request.POST.get("title")
            and request.POST.get("start")
            and request.POST.get("end")
            and request.POST.get("painting")
        ):
            title = request.POST.get("title")
            start = request.POST.get("start")
            end = request.POST.get("end")
            painting = Painting.objects.get(id=request.POST.get("painting"))
            exhibition = Exhibition(title=title, start=start, end=end, writer=request.user.writer, painting=painting)
            exhibition.save()
            return redirect("accounts:my_writer")
        else:
            context["error"] = "등록 입력사항을 다시 확인해주세요!"
            return render(request, "accounts/my_writer_exhibition.html", context)
    else:
        paintings = Painting.objects.filter(writer=request.user.writer)

        context = {
            "paintings": paintings,
        }

        return render(request, "accounts/my_writer_exhibition.html", context)
