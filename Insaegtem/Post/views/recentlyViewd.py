from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from ..serializers.recentlyviewd import RecentlyViewdSerializer
from ..models.recentlyviewd import RecentlyViewd
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from rest_framework import serializers


# TO DO : put 요청 시에 타임스탬프 시간 바꿔주기
class RecentlyViewdViewSet(viewsets.ModelViewSet):
    queryset = RecentlyViewd.objects.all()
    serializer_class = RecentlyViewdSerializer
