from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from ..serializers.bookmark import BookMarkSerializer
from ..models.bookmark import BookMark
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework import serializers


class BookMarkViewSet(viewsets.ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    # TO DO: user_id 받아와서 user_id 북마크만 띄워주기
    def list(self, request, *args, **kwargs):
        bookmark_user_id = request.data.get("user_id")

        queryset = self.get_queryset()
        queryset = queryset.filter(user_id=bookmark_user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        bookmark_user_id = request.data.get("user_id")
        bookmark_post_id = request.data.get("post_id")

        bookmark = BookMark.objects.create(user_id=bookmark_user_id, post_id=bookmark_post_id)

        serialized_obj = serializers.serialize('json', [bookmark, ])

        return HttpResponse(serialized_obj, content_type="application/json")
