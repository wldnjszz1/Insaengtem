from rest_framework import serializers
from ..models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        feilds = '__all__'
