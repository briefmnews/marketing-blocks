from __future__ import unicode_literals

from django import forms
from django.conf import settings
from django.contrib import admin

from .models import MarketingBlock

MARKETING_BLOCKS_LABEL_CHOICES = getattr(settings, "MARKETING_BLOCKS_LABEL_CHOICES", "")


class MarketingBlocksAdminForm(forms.ModelForm):
    label = forms.ChoiceField(choices=MARKETING_BLOCKS_LABEL_CHOICES, required=False)

    class Meta:
        model = MarketingBlock
        fields = "__all__"


class MarketingBlocksAdmin(admin.ModelAdmin):
    list_display = ("label", "title", "position", "active", "modified")
    list_filter = ("position", "label")
    form = MarketingBlocksAdminForm


admin.site.register(MarketingBlock, MarketingBlocksAdmin)
