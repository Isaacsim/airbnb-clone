from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):  # user 처럼 기존에 작성된 상속이 없을 때는 models.Model을 가져온다

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # auto_now : 필드가 모델을 기록할때의 값을 기록함 // auto_now_add :모델을 생성할 때의 값을 기록함

    class Meta:
        abstract = True

    # 타임스탬프를 사용하는 모든 클래스가 호출될 때 db에 올라가는 것을 방지하기 위해
    # Meta abstract값을 준다 <= 이러면 해당 클래스는 사용될 때 db에 안올라감 : 코드에서만 사용
    # User API에는 이미 타임스탬프 기능이 있기 때문에 이를 사용하지 않음
