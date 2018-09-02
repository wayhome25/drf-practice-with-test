from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(APIView):
    """List all code snippets, or create a new snippet"""

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(instance=snippets, many=True)
        return Response(data=serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """Retrieve, update or delete a code snippet."""

    def get_object(self, pk):
        return get_object_or_404(Snippet, pk=pk)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(instance=snippet)
        return Response(data=serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serialzier = SnippetSerializer(instance=snippet, data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(data=serialzier.data)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
