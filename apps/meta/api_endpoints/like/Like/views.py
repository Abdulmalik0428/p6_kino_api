from rest_framework.views import APIView
from rest_framework.response import Response

from apps.meta.api_endpoints.like.Like.serializers import LikeSerializer


class LikeView(APIView):
    def post(self, request):
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({'status': 'ok'})