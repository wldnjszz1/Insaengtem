from rest_framework import serializers
from ..models.bookmark import BookMark


class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        feilds = '__all__'
