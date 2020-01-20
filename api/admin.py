from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Restaurant)
admin.site.register(models.Recipe)
admin.site.register(models.Ingredient)
