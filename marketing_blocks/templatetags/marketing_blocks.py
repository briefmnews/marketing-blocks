from django import template
from django.utils.safestring import mark_safe

from marketing_blocks.models import MarketingBlock


register = template.Library()


@register.simple_tag(takes_context=True)
def render_marketing_block(context, obj, position):
    if context.get("hide_marketing"):
        return ""

    block = MarketingBlock.objects.get_active_block_for_position_and_label(
        label=obj._meta.model_name, position=position
    )

    return mark_safe(block.content if block else "")
