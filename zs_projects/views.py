from zs_projects.models import Projects
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
class ProjectList(ListView):
    template_name = 'home_page.html'

    def get_queryset(self):
        return Projects.objects.all()
