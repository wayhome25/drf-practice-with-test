import factory
from django.contrib.auth.models import User

from snippets.models import Snippet


class UserFactory(factory.DjangoModelFactory):
    username = factory.Faker('user_name')

    class Meta:
        model = User


class SnippetFactory(factory.DjangoModelFactory):
    owner = UserFactory()
    title = factory.Sequence(lambda n: "test {}".format(n))
    code = factory.lazy_attribute(lambda snippet: "print('test_code: {}')".format(snippet.title))

    class Meta:
        model = Snippet
