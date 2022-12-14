# Generated by Django 4.1 on 2022-08-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=100, unique=True, verbose_name="이메일")),
                ("password", models.CharField(max_length=128, verbose_name="비밀번호")),
                ("username", models.CharField(max_length=16, verbose_name="이름")),
                ("gender", models.CharField(max_length=2, verbose_name="성별")),
                ("mobile", models.CharField(max_length=20, verbose_name="연락처")),
                ("birth", models.DateField(verbose_name="생년월일")),
                ("is_active", models.BooleanField(default=True, verbose_name="활성화")),
                ("is_admin", models.BooleanField(default=False, verbose_name="관리자")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="작성시간")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정시간")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
