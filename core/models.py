from django.db import models


class TimeStampedModel(models.Model):
    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # 모델이 생성된 날짜를 구해줌
    updated = models.DateTimeField(auto_now=True)  # 모델이 업데이트 된 날짜를 구해줌

    class Meta:
        abstract = True  # 타임스탬프모델 클래스가 추상모델로써 데이터베이스에 등록하지 않게 해주는 클래스
