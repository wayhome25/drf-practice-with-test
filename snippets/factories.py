import factory

from snippets.models import Snippet


class SnippetFactory(factory.DjangoModelFactory):
    title = factory.Sequence(lambda n: "test {}".format(n))
    code = factory.lazy_attribute(lambda snippet: "print('test_code: {}')".format(snippet.title))

    class Meta:
        model = Snippet
