from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(ListCreateAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(RetrieveUpdateDestroyAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
