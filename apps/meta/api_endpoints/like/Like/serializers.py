from rest_framework import serializers
from apps.meta.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "movie", "watch_session"]
