# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import MarketingBlock


class MarketingBlocksAdmin(admin.ModelAdmin):
    list_display = ("title", "position", "active", "modified")
    list_filter = ("position",)


admin.site.register(MarketingBlock, MarketingBlocksAdmin)
