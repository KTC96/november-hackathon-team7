from django.shortcuts import render
from django.views import generic, View
from models.py import Achievement


# Create your views here.
class AchievementList(generic.ListView):
    model = Achievement
    queryset = Category.objects.order_by('-category_id')

from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'index.html'
