from django.test import TestCase
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from snippets.factories import SnippetFactory
from snippets.models import Snippet


class SnippetListTestCase(APITestCase):

    def setUp(self):
        for _ in range(10):
            SnippetFactory()

    def test_get_snippet_목록확인(self):
        response = self.client.get(reverse('snippet_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)

    def test_post_snippet_생성확인(self):
        response = self.client.post(reverse('snippet_list'), data={'code': 'print("hello world")'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 11)
        self.assertEqual(Snippet.objects.last().code, 'print("hello world")')
