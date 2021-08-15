# Custom Commands 주요 작성은 오버라이딩으로 이루어진다.
# 이해가 정말 어렵다.
from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command created facilities"

    """     def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many times do you want me to tell you that I love you?"
        )
        """

    def handle(self, *args, **options):  # 어메니티를 어드민페이지에서 수동(노가다)으로 안하고 코드로 작성하는 방법
        facilites = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilites:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilites)} facilites created"))

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
