# 장고, 써드파티, 내패키지 순으로 임포트

from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    # 다대다 속성을 가지는 아이템을 설정하기 위한 클래스

    def __str__(self):
        return self.name  # 이름만 보여지게함


class RoomType(AbstractItem):

    """ Room Type Model Definition """

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ House Rule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=50)
    file = models.ImageField()
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


# Create your models here.
class Room(core_models.TimeStampedModel):

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )  # 7.1 related_name : 유저가 어떻게 이 관계를 찾을것인가, 이름 설정
    # 유저가 삭제되면 이에 해당되는 룸도 같이 삭제되게 하는 관계. 종속관계 (반대관계는 PROTECT, 종속이 있으면 삭제되지 않음)
    # 일대다필드. room에선 user의 정보를 받고, user는 room의 정보를 받지 않음
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facillities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)
    # 다대다필드는 _set이 아닌 파라미터값으로 바로 접근이 가능하다. 즉, related_name=self)
    # startswith = User.objects.filter(username__startswith="i")
    def __str__(self):
        return self.name  # admin에서 보여지는 경로에서 object(n)이 아닌 이름으로 표기하게 해줌
