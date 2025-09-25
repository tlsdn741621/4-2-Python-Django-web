from django.db import models

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    # 객체 출력시, 설정을 하면, 설정된 이름으로 출력,
    # 미설정: 객체로 표기.
    def __str__(self):
        return self.name