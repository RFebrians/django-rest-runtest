from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Birthday)
admin.site.register(models.Password)
admin.site.register(models.Todo)