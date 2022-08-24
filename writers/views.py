from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Painting, Writer


# url : GET writers/
def list(request):
    """
    Assignee : 상백

    작가 목록을 조회할 수 있는 페이지 구현
    최근에 등록된 순서대로 조회할 수 있게 ORM 메소드인 order_by를 created_at 내림차순으로 설정하고
    작가 등록 신청이 완료된 작가들만 보여주기 위해 approval=True 필터링 조건 설정
    작가 이름, 성별, 생년월일, 연락처 정보 응답
    """

    writers = Writer.objects.filter(approval=True).order_by("-created_at")

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


# url : GET,POST writers/register/
@login_required
def register(request):
    """
    Assignee : 상백

    GET : 작가 등록 신청을 할 수 있는 페이지 구현
    @login_required로 로그인을 해야 접근할 수 있게 설정
    로그인이 된 이후에는, 작가 등록 승인이 되지 않은 상황이면 접근이 가능하고 승인이 되었다면 작가 리스트 화면으로 redirect 하게끔 설정
    POST : 작가 등록 신청 로직 구현
    html의 input - type 요소를 이용해서 이름 16자 이하 / 성별 남여 선택 / 이메일 형식 / 생년월일 캘린더 선택 / 연락처 pattern 지정으로
    입력 정보 형식 설정
    위의 정보가 하나라도 없을 경우 context에 에러 메시지 추가해서 html에 보여주도록 설정
    신청 단계로 approval 필드는 False로 지정
    """

    context = {}

    if hasattr(request.user, "writer"):
        if request.user.writer.approval == False:
            return render(request, "writers/register.html", context)
        else:
            return redirect("writers:list")
    else:
        if request.method == "POST":
            if (
                request.POST.get("name")
                and request.POST.get("gender")
                and request.POST.get("birth")
                and request.POST.get("email")
                and request.POST.get("mobile")
            ):
                user = request.user
                name = request.POST.get("name")
                gender = request.POST.get("gender")
                birth = request.POST.get("birth")
                email = request.POST.get("email")
                mobile = request.POST.get("mobile")
                writer = Writer(
                    user=user, name=name, gender=gender, birth=birth, email=email, mobile=mobile, approval=False
                )
                writer.save()
                return redirect("writers:list")
            else:
                context["error"] = "등록 입력사항을 다시 확인해주세요!"
                return render(request, "writers/register.html", context)
        else:
            return render(request, "writers/register.html", context)
