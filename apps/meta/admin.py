from django.contrib import admin

from apps.meta.models import WatchSession,Like,Comment


admin.site.register(WatchSession)
admin.site.register(Like)
admin.site.register(Comment)