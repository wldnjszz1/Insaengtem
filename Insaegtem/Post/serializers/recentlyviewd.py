from rest_framework import serializers
from ..models.recentlyviewd import RecentlyViewd


class RecentlyViewd(serializers.ModelSerializer):
    class Meta:
        model = RecentlyViewd
        feilds = '__all__'
