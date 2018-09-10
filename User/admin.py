from django.contrib import admin
from User import models


admin.site.register(models.Students)
admin.site.register(models.Teachers)
admin.site.register(models.UserProfile)
admin.site.register(models.Leader)