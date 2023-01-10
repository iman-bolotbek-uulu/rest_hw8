from django.contrib import admin

from . import models

admin.site.register(models.StateType)
admin.site.register(models.StatusTweet)
admin.site.register(models.StatusComment)
admin.site.register(models.Tweet)
admin.site.register(models.Comment)