from rest_framework.response import Response
from rest_framework.views import APIView
from apps.meta.models import Like
from apps.meta.api_endpoints.like.Like.serializers import LikeSerializer


class LikeView(APIView):
    def post(self, request, pk):
        data = {"movie": pk}
        serializer = LikeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk):
        count = Like.objects.filter(movie_id=pk).count()
        return Response({"movie_id": pk, "likes_count": count})

    def delete(self, request, pk):
        like = Like.objects.filter(movie_id=pk).last()
        if like:
            like.delete()
            return Response({"status": "unliked"})
        return Response({"error": "Like not found"})
