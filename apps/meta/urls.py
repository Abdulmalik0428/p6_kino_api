from django.urls import path
from apps.meta.api_endpoints import watchsession,like,comment


urlpatterns = [
    path('watch-session-create/',
         watchsession.WatchSessionCreateView.as_view(),
         name='watch_session_create'),
    path('like/',
        like.LikeView.as_view(),
        name='like'),
    path('comment/',
        comment.CommentView.as_view(),
        name='comment'),
]
