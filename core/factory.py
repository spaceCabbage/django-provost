import factory
from factory.faker import faker
from .models import Post, Comment
from django.contrib.auth.models import User


FAKE = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence", nb_words=4)
    content = factory.Faker("text")
    user = factory.Iterator(User.objects.all())


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Faker("text")
    user = factory.Iterator(User.objects.all())
    post = factory.Iterator(Post.objects.all())
