# 지금은 django 설치 안해서, 일단, 아무거나 임포트 한 상태임. 
from pip._internal import models


class DjangoModel(models.Model):
    name = models.CharField(max_length=100)
