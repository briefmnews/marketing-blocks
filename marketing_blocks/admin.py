from django import forms
from django.conf import settings
from django.contrib import admin

from .models import MarketingBlock

MARKETING_BLOCKS_LABEL_CHOICES = getattr(settings, "MARKETING_BLOCKS_LABEL_CHOICES", "")
MARKETING_BLOCKS_ADMIN_BUTTONS = getattr(settings, "MARKETING_BLOCKS_ADMIN_BUTTONS", [])


class MarketingBlocksAdminForm(forms.ModelForm):
    label = forms.ChoiceField(choices=MARKETING_BLOCKS_LABEL_CHOICES, required=False)

    class Meta:
        model = MarketingBlock
        fields = "__all__"


class MarketingBlocksAdmin(admin.ModelAdmin):
    list_display = ("label", "title", "position", "active", "modified")
    list_filter = ("position", "label")
    search_fields = ("title",)
    form = MarketingBlocksAdminForm

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["buttons"] = MARKETING_BLOCKS_ADMIN_BUTTONS
        return super().changelist_view(request, extra_context=extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context["buttons"] = MARKETING_BLOCKS_ADMIN_BUTTONS
        return super().change_view(request, object_id, form_url, extra_context)


admin.site.register(MarketingBlock, MarketingBlocksAdmin)
