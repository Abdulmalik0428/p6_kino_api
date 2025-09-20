from rest_framework.views import APIView
from rest_framework.response import Response
from apps.meta.models import Comment
from apps.meta.api_endpoints.comment.Comment.serializers import CommentSerializer

class CommentView(APIView):
    def get(self, request, movie_id):
        comments = Comment.objects.filter(movie_id=movie_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, movie_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie_id=movie_id)
            return Response(serializer.data)
        return Response(serializer.errors)


class CommentDetailView(APIView):
    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response({"detail": "Comment deleted"})


