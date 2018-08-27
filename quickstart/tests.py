from django.contrib.auth.models import User
from django.test import TestCase
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase

from quickstart.views import UserViewSet


class UserViewSetTestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create(username='test1', password='test_pw_1')
        self.user2 = User.objects.create(username='test2', password='test_pw_2')
        self.user3 = User.objects.create(username='test3', password='test_pw_3')

    def test_get_유저목록_가져오기(self):

        # API client 활용
        response_1 = self.client.get(reverse('user-list'))

        self.assertEquals(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_1.data), 3)
        self.assertContains(response_1, self.user1.username)
        self.assertContains(response_1, self.user2.username)
        self.assertContains(response_1, self.user3.username)

        # APIRequestFactory 활용
        factory = APIRequestFactory()
        view = UserViewSet.as_view({'get': 'list'})
        request = factory.get(reverse('user-list'))
        response_2 = view(request)

        self.assertEqual(len(response_2.data), 3)
        self.assertContains(response_2, self.user1.username)
        self.assertContains(response_2, self.user2.username)
        self.assertContains(response_2, self.user3.username)

    def test_post_유저_생성하기(self):

        # API client 활용
        response_1 = self.client.post(reverse('user-list'), data={"username": "test4", "password": "test_pw_4"})

        self.assertEquals(response_1.status_code, status.HTTP_201_CREATED)
        self.assertEquals(User.objects.count(), 4)
        self.assertEquals(User.objects.last().username, 'test4')

        # APIRequestFactory 활용
        factory = APIRequestFactory()
        view = UserViewSet.as_view({'post': 'create'})
        request = factory.post(reverse('user-list'),  data={"username": "test5", "password": "test_pw_5"}, format='json')
        response_2 = view(request)

        self.assertEquals(response_2.status_code, 201)
        self.assertEquals(response_2.data.get('username'), 'test5')

