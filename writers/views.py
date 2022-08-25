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
    작가로 승인된 작가의 작품들만 볼 수 있게 html에 django template language 설정
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


# url : GET writers/admin/
def admin(request):
    """
    Assignee : 상백

    관리자 대시보드 페이지 구현
    해당 페이지에서 작가 등록 신청 내역 조회 페이지 및 작가 통계 페이지로 이동할 수 있게 a element 설정
    관리자만 해당 페이지를 볼 수 있게 if문 설정
    """

    if request.user.is_admin == True:
        return render(request, "writers/admin.html")
    else:
        return redirect("writers:list")


# url : GET,POST writers/admin/register/
def admin_register(request):
    """
    Assignee : 상백

    GET : 작가 등록 신청 내역을 조회할 수 있는 페이지 구현
    신청자 정보를 최신순으로 표기
    POST : 작가 등록 신청 승인 로직 구현
    원하는 신청자 체크박스 선택 후 버튼 클릭 시, 신청자 id 정보를 받아 조회하고 approval 필드가 False일 경우에만 True로 수정해서 승인 진행
    승인 완료 후에는 작가 리스트에 추가됨을 확인하기 위해 작가 목록 리스트 redirect
    """

    if request.method == "POST":
        register_id = request.POST.get("admin_register")
        writer = Writer.objects.get(id=register_id)
        if writer.approval == False:
            writer.approval = True
            writer.save()
            return redirect("writers:list")
    else:
        writers = Writer.objects.filter(approval=False).order_by("-created_at")

    writers = Writer.objects.filter(approval=False).order_by("-created_at")
    context = {
        "writers": writers,
    }

    return render(request, "writers/admin_register.html", context)


# url : GET writers/admin/statistics/
def admin_statistics(request):
    """
    Assignee : 상백

    작가 통계 페이지 구현
    등록된 총 작품 개수 / 등록된 총 작가 수 / 승인대기 중인 작가 수 응답
    요구사항인 작가별 100호 이하 작품 개수 및 작품 평균 가격은 구현하지 못함
    """

    paintings_count = Painting.objects.all().count()
    writers_count = Writer.objects.filter(approval=True).count()
    before_writers_count = Writer.objects.filter(approval=False).count()
    writers = Writer.objects.filter(approval=True).order_by("-created_at")

    context = {
        "paintings_count": paintings_count,
        "writers_count": writers_count,
        "before_writers_count": before_writers_count,
        "writers": writers,
    }

    return render(request, "writers/admin_statistics.html", context)
