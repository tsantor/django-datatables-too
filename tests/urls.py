# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.urls import path  # include
from django.contrib import admin

urlpatterns = [
    path(r'admin/', admin.site.urls),
    # path(r'', include('django_perm_filter.urls')),
]
