# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import RestaurantLocation
from django.views import View
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

# Create your views here.
# function based views


def restaurant_view(request):
    template_name = "restaurant/restaurantlocation_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {'context_list': queryset}
    return render(request, template_name, context)


def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        # django forms
        # RestaurantLocation.objects.create(
        #     name=form.cleaned_data.get('name'),
        #     location=form.cleaned_data.get('location'),
        #     category=form.cleaned_data.get('category'),
        # )
        # model form
        form.save()
        return HttpResponseRedirect('/restaurant/')
    if form.errors:
        errors = form.errors
    template_name = "restaurant/form.html"
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                                Q(category__iexact=slug) |
                                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     #id = self.kwargs.get("id")
    #     print(self.kwargs)
    #     #Why this is done?
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj


class RestaurantLocationCreate(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurant/form.html'
    success_url = '/restaurant/'
