# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class HomePageView(TemplateView):
#	def get(self, request, **kwargs):
#		return render(request, 'index.html', context=None)

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ThePlanView(TemplateView):
    template_name ='plan.html'
