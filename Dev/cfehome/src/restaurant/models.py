# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.


class RestaurantLocation(models.Model):
    name        = models.CharField(max_length=120)
    category    = models.CharField(max_length=120, blank=True, null=True)
    location    = models.CharField(max_length=120, blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def rl_pre_save_receiver(sender,instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# def rl_post_save_receiver(sender,instance,created,*args,**kwargs):
#     print('saved')
#     print(instance.timestamp)


pre_save.connect(rl_pre_save_receiver, RestaurantLocation)
# post_save.connect(rl_post_save_receiver, RestaurantLocation)