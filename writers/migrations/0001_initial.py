# Generated by Django 4.1 on 2022-08-21 06:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Writer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=16, verbose_name="이름")),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=10, verbose_name="성별"
                    ),
                ),
                ("birth", models.DateField(verbose_name="생년월일")),
                ("email", models.EmailField(max_length=100, unique=True, verbose_name="이메일")),
                ("mobile", models.CharField(max_length=20, verbose_name="연락처")),
                ("approval", models.BooleanField(default=False, verbose_name="작가등록여부")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="등록일자")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일자")),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="accounts.user")),
            ],
        ),
        migrations.CreateModel(
            name="Painting",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=64, verbose_name="제목")),
                ("price", models.PositiveIntegerField(default=0, verbose_name="가격")),
                (
                    "size",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(500),
                        ],
                        verbose_name="호수",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="등록일자")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일자")),
                (
                    "writer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="writer_painting", to="writers.writer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exhibition",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=64, verbose_name="제목")),
                ("start", models.CharField(max_length=12, verbose_name="시작일")),
                ("end", models.CharField(max_length=12, verbose_name="종료일")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="등록일자")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일자")),
                (
                    "writer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="writer_exhibition",
                        to="writers.writer",
                    ),
                ),
            ],
        ),
    ]
