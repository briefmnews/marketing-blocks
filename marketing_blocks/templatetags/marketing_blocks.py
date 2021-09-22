from django import template
from django.utils.safestring import mark_safe

from marketing_blocks.models import MarketingBlock


register = template.Library()


@register.simple_tag(takes_context=True)
def render_marketing_block(context, obj, position):
    block = MarketingBlock.objects.get_active_block_for_position_and_label(
        label=obj._meta.model_name, position=position
    )

    if block and not context.get("hide_marketing"):
        block = block.content
    else:
        block = ""

    return mark_safe(block)
