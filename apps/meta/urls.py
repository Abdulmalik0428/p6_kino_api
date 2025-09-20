from django.urls import path
from apps.meta.api_endpoints import watchsession,like,comment


urlpatterns = [
    path('watch-session-create/',
         watchsession.WatchSessionCreateView.as_view(),
         name='watch_session_create'),
    path('movie/<int:pk>/likes/',
        like.LikeView.as_view(),
        name='like'),
    path('movie/<int:movie_id>/comments/',
        comment.CommentView.as_view(),
        name='comment'),
]
