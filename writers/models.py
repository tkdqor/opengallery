from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from accounts.models import User


class Writer(models.Model):
    """
    Assignee : 상백

    User 모델과 1:1 관계가 형성되어 있는 Writer 작가 모델 정의
    성별은 남/여 선택할 수 있도록 카테고리 설정
    작가 등록 시 approval 필드 True로 변경하고 해당 작가와 문제가 있을 경우, False로 등록 보류 가능하도록 설정
    """

    class Category(models.TextChoices):
        male = "male"
        female = "female"

    name = models.CharField("이름", max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField("성별", max_length=10, choices=Category.choices)
    birth = models.DateField("생년월일")
    email = models.EmailField("이메일", max_length=100, unique=True)
    mobile = models.CharField("연락처", max_length=20)
    approval = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField("등록일자", auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)


class Painting(models.Model):
    """
    Assignee : 상백

    Writer 모델과 1:N 관계가 형성되어 있는 Painting 작품 모델 정의
    가격은 0 이상, 호수는 1 이상 500 이하의 숫자를 설정하기 위해 django에서 제공하는 validator 사용
    """

    title = models.CharField("제목", max_length=64)
    writer = models.ForeignKey("Writer", on_delete=models.CASCADE, related_name="writer_painting")
    price = models.PositiveIntegerField("가격", default=0)
    size = models.IntegerField("호수", validators=[MinValueValidator(1), MaxValueValidator(500)])
    created_at = models.DateTimeField("등록일자", auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)


class Exhibition(models.Model):
    """
    Assignee : 상백

    Writer 모델과 1:N 관계가 형성되어 있는 Exhibition 전시 모델 정의
    """

    title = models.CharField("제목", max_length=64)
    writer = models.ForeignKey("Writer", on_delete=models.CASCADE, related_name="writer_exhibition")
    painting = models.OneToOneField(Painting, on_delete=models.PROTECT, null=True)
    start = models.CharField("시작일", max_length=12)
    end = models.CharField("종료일", max_length=12)
    created_at = models.DateTimeField("등록일자", auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)
