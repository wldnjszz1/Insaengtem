from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from ..serializers.post import PostSerializer
from ..models.post import Post
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework import serializers


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

        # TO DO: 존재하지 않는 경우 null값으로 어떻게 넘겨줄것인지(존재할 경우에만 값 받아오기)
        post = Post.objects.create(
            user_id=post_user_id, image=post_image, description=post_description,
            category1=post_category1, category2=post_category2, category3=post_category3,
            category4=post_category4, category5=post_category5, category6=post_category6,
            category7=post_category7, category8=post_category8, category9=post_category9,
            category10=post_category10
        )

        serialized_obj = serializers.serialize('json', [post, ])

        return HttpResponse(serialized_obj, content_type="application/json")

    # TO DO: 유저만 게시물을 삭제, 수정할 수 있게 하기
    def destroy(self, request, *args, **kwargs):

