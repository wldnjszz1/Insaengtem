from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from ..serializers.post import PostSerializer
from ..models.post import Post
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.core import serializers
from Auth.models import IstUser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        post_user_id = request.data.get("user_id")
        post_image = request.data.get("image")
        post_description = request.data.get("description")
        post_category1 = request.data.get("1")
        post_category2 = request.data.get("2")
        post_category3 = request.data.get("3")
        post_category4 = request.data.get("4")
        post_category5 = request.data.get("5")
        post_category6 = request.data.get("6")
        post_category7 = request.data.get("7")
        post_category8 = request.data.get("8")
        post_category9 = request.data.get("9")
        post_category10 = request.data.get("10")

        user_id = IstUser.objects.get(pk=post_user_id)

        post = Post.objects.create(
            user_id=user_id, image=post_image, description=post_description,
            category1=post_category1, category2=post_category2, category3=post_category3,
            category4=post_category4, category5=post_category5, category6=post_category6,
            category7=post_category7, category8=post_category8, category9=post_category9,
            category10=post_category10
        )

        serialized_obj = serializers.serialize('json', [post, ])

        return HttpResponse(serialized_obj, content_type="application/json")

    # TO DO: 유저만 게시물을 삭제, 수정할 수 있게 하기
    #def destroy(self, request, *args, **kwargs):

    # TO DO: 태그가 트루인 포스트만 보여주기
    def search_tag(self, request):
        tag1 = request.data.get("1")
        tag2 = request.data.get("2")
        tag3 = request.data.get("3")
        tag4 = request.data.get("4")
        tag5 = request.data.get("5")
        tag6 = request.data.get("6")
        tag7 = request.data.get("7")
        tag8 = request.data.get("8")
        tag9 = request.data.get("9")
        tag10 = request.data.get("10")

        if tag1:
            queryset = self.get_queryset()
            queryset = queryset.filter(category1=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag2:
            queryset = self.get_queryset()
            queryset = queryset.filter(category2=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag3:
            queryset = self.get_queryset()
            queryset = queryset.filter(category3=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag4:
            queryset = self.get_queryset()
            queryset = queryset.filter(category4=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag5:
            queryset = self.get_queryset()
            queryset = queryset.filter(category5=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag6:
            queryset = self.get_queryset()
            queryset = queryset.filter(category6=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag7:
            queryset = self.get_queryset()
            queryset = queryset.filter(category7=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag8:
            queryset = self.get_queryset()
            queryset = queryset.filter(category8=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag9:
            queryset = self.get_queryset()
            queryset = queryset.filter(category9=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if tag10:
            queryset = self.get_queryset()
            queryset = queryset.filter(category10=True)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)



    # TO DO: 특정 유저가 쓴 글만 보여주기



