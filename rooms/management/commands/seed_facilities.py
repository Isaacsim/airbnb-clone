from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates facilities"

    # def add_arguments(self, parser):
    #   parser.add_argument(
    #       "--times", help="how many times do you want to tell you how i loved"
    #   )
    #
    #   times = options.get("times")
    #   for time in range(0, int(times)):
    #       self.stdout.write(self.style.SUCCESS("I love you"))
    #   print(args, options)

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for a in facilities:
            room_models.Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
