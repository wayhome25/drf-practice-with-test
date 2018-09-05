from rest_framework import status
from rest_framework.test import APITestCase

from django.urls.base import reverse

from snippets.factories import SnippetFactory
from snippets.factories import UserFactory
from snippets.models import Snippet


class SnippetListTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        for _ in range(10):
            SnippetFactory()

    def test_get_snippet_목록확인(self):
        response = self.client.get(reverse('snippet-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 10)

    def test_post_snippet_성공(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('snippet-list'), data={'code': 'print("hello world")'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 11)
        self.assertEqual(response.data['code'], 'print("hello world")')
        self.assertEqual(response.data['owner'], self.user.username)

    def test_post_snippet_실패_400에러(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('snippet-list'), data={})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_snippet_실패_403에러(self):
        response = self.client.post(reverse('snippet-list'), data={'code': 'print("hello world")'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SnippetDetailTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user_1 = UserFactory()
        cls.user_2 = UserFactory()

    def setUp(self):
        self.snippet = SnippetFactory(pk=1, owner=self.user_1)

    def test_get_성공(self):
        response = self.client.get(reverse('snippet-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], self.snippet.code)

    def test_존재하지_않는_snippet(self):
        response = self.client.get(reverse('snippet-detail', args=[2]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_성공(self):
        self.client.force_login(self.user_1)
        resposne = self.client.put(reverse('snippet-detail', args=[1]), data={'code': 'edited code'})
        self.assertEqual(resposne.status_code, status.HTTP_200_OK)
        self.assertEqual(resposne.data['code'], 'edited code')

    def test_put_실패_400에러(self):
        self.client.force_login(self.user_1)
        resposne = self.client.put(reverse('snippet-detail', args=[1]), data={'title': 'edited title'})
        self.assertEqual(resposne.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_실패_403에러_권한없음(self):
        self.client.force_login(self.user_2)
        resposne = self.client.put(reverse('snippet-detail', args=[1]), data={'title': 'edited title'})
        self.assertEqual(resposne.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_성공(self):
        self.client.force_login(self.user_1)
        resposne = self.client.delete(reverse('snippet-detail', args=[1]))
        self.assertEqual(resposne.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_실패_403에러_권한없음(self):
        self.client.force_login(self.user_2)
        response = self.client.delete(reverse('snippet-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
