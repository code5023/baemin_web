from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Partner(models.Model):
    KOREAN_FOOD = "ko"
    CHINESE_FOOD = "cn"
    JAPANESE_FOOD = "jp"

    CATEGORIES = (
        (KOREAN_FOOD, "한식"),
        (CHINESE_FOOD, "중식"),
        (JAPANESE_FOOD, "일식")
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50,
        verbose_name="업체 이름"
    )
    contact = models.CharField(
        max_length=50,
        verbose_name="연락처"
    )
    address = models.CharField(
        max_length=200,
        verbose_name="주소"
    )
    description = models.TextField(
        verbose_name="상세 소개"
    )
    active = models.BooleanField()
    category = models.CharField(
        max_length=10,
        choices=CATEGORIES,
        default=KOREAN_FOOD,
        verbose_name="음식 종류"
    )

    def __str__(self):
        return "[{}], {}".format(self.name, self.address)

class Menu(models.Model):
    partner = models.ForeignKey(
        Partner, on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name="메뉴 이미지"
    )
    name = models.CharField(
        max_length=50,
        verbose_name="메뉴 이름"
    )
    price = models.PositiveIntegerField(
        verbose_name="가격"
    )
