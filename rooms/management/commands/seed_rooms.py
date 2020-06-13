import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates many rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="how many rooms do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
                "price": lambda x: random.randint(1, 1000),
            },
        )
        # 9.4 PK 항목의 seeder 생성, execute가 keys를 반복하여 1~10까지 리턴하는 것을 이용
        created_photos = seeder.execute()
        # 9.4 flatten으로 2차 행렬을 1차로 빼옴
        created_clean = flatten(list(created_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facillities = room_models.Facility.objects.all()
        house_rules = room_models.HouseRule.objects.all()

        for pk in created_clean:
            # 9.4 생성된 room의 위치를 pk로 찾음. execute의 리턴값이 pk임을 이용
            room = room_models.Room.objects.get(pk=pk)
            for i in range(random.randint(3, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                    room=room,
                )
                # 9.5 ManyToManyField 관계의 seed 생성
            for a in amenities:
                magic_num = random.randint(0, 15)
                if magic_num % 3 == 0:
                    room.amenities.add(a)
            for f in facillities:
                magic_num = random.randint(0, 15)
                if magic_num % 3 == 0:
                    room.facillities.add(f)
            for r in house_rules:
                magic_num = random.randint(0, 15)
                if magic_num % 3 == 0:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
