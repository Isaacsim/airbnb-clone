from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "price",)},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book",)},),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)},),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facillities", "house_rules",),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    # relationship, 함수, manytomanyfields를 리스트업하기 위한 부분
    #
    def count_amenities(self, obj):  # self는 모클래스, object는 데이터의 현재 행
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    # 정렬
    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "host__superhost",
        "instant_book",
        "city",
        "room_type",
        "amenities",
        "facillities",
        "house_rules",
        "country",
    )

    search_fields = [
        "city",
        "^host__username",
    ]

    filter_horizontal = (
        "amenities",
        "facillities",
        "house_rules",
    )
    # icontains, startswith, exact, search 등
    pass


# dir : 클래스 안의 리스트 이름을 리턴 / vars : 클래스 리스트 안의 것을 리턴
# 쿼리 : list of objects

# 7.0 user는 room, reviews, lists, messages 에 foreignkey 연결을 가지고 있다. -> vars로 ._set을 볼 수 있음
# admin 창에서는 유저 정보안에 room에 대한 정보가 없지만, 코드에서는 room_set이라는 코드로 엑세스한다. : 장고가 자동으로 생성한 것
# sis = User.objects.get(username="isaacsim")
# vars(sis), dir(sis) ==> 모델이름_set
