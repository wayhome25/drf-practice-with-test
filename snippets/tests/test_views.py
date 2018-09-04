from rest_framework import status
from rest_framework.test import APITestCase

from django.urls.base import reverse

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

    def test_post_snippet_성공(self):
        response = self.client.post(reverse('snippet_list'), data={'code': 'print("hello world")'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 11)
        self.assertEqual(Snippet.objects.last().code, 'print("hello world")')

    def test_post_snippet_실패(self):
        response = self.client.post(reverse('snippet_list'), data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SnippetDetailTestCase(APITestCase):

    def setUp(self):
        self.snippet = SnippetFactory(pk=1)

    def test_get_성공(self):
        response = self.client.get(reverse('snippet_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], self.snippet.code)

    def test_존재하지_않는_snippet(self):
        response = self.client.get(reverse('snippet_detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_성공(self):
        resposne = self.client.put(reverse('snippet_detail', args=[1]), data={'code': 'edited code'})
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)
        self.assertEqual(resposne.data['code'], 'edited code')

    def test_put_실패(self):
        resposne = self.client.put(reverse('snippet_detail', args=[1]), data={'title': 'edited title'})
        self.assertEqual(resposne.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_성공(self):
        resposne = self.client.delete(reverse('snippet_detail', args=[1]))
        self.assertEqual(resposne.status_code, status.HTTP_204_NO_CONTENT)
