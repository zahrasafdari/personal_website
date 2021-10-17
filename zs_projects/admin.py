from zs_projects.models import Projects
from django.contrib import admin

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title']


admin.site.register(Projects,ProjectAdmin)
