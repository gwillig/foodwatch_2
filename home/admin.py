from django.contrib import admin
from .models import Misc,Food,HomeValue


# class TodoAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'completed')
#
#
# Register your models here.
admin.site.register(Misc)
admin.site.register(Food)
admin.site.register(HomeValue)
