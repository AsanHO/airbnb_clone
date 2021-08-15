# Custom Commands 주요 작성은 오버라이딩으로 이루어진다.
# 이해가 정말 어렵다.
from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command tells me that he loves me"

    """     def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
        """

    def handle(self, *args, **options):  # 어메니티를 어드민페이지에서 수동(노가다)으로 안하고 코드로 작성하는 방법
        amenities = [
            "Air conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon monoxide detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double bed",
            "En suite bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen size bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))

    """
    class Command(BaseCommand):

        help = "This command tells me that he loves me"
        from django.core.management.base import BaseCommand

        def add_arguments(self, parser):
            parser.add_argument(
                "--times", help="How many times do you want me to tell you that I love you?"
            )

        def handle(self, *args, **options):
            times = options.get("times")
            for t in range(0, int(times)):
                self.stdout.write(self.style.SUCCESS("I love you"))"""
