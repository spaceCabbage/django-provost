from django.core.management.base import BaseCommand
from core.factory import UserFactory, PostFactory, CommentFactory


class Command(BaseCommand):
    help = "Populates the database with sample data"

    def handle(self, *args, **options):
        users = UserFactory.create_batch(size=20)
        posts = PostFactory.create_batch(size=100)
        comments = CommentFactory.create_batch(size=300)

        self.stdout.write(
            self.style.SUCCESS("Successfully populated the database with sample data")
        )
