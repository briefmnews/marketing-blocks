import pytest

from django.template import Context, Template

from marketing_blocks.models import MarketingBlock
from marketing_blocks.templatetags.marketing_blocks import render_marketing_block

pytestmark = pytest.mark.django_db(transaction=True)


class TestMarketingBlockTags:
    def test_tag_render_active_block(self, issue, active_header_block):
        # GIVEN
        template = "{% load marketing_blocks %}{% render_marketing_block obj 'header' %}"

        # WHEN
        out = Template(template).render(Context({"obj": issue}))

        # THEN
        assert out == "<p>I'm an active header</p>"

    def test_tag_fail_silently_when_block_does_not_exist(self, issue, active_header_block):
        # GIVEN
        template = "{% load marketing_blocks %}{% render_marketing_block obj 'schrodinger' %}"
        assert not MarketingBlock.objects.filter(position="schrodinger").count()

        # WHEN
        out = Template(template).render(Context({"obj": issue}))

        # THEN
        assert out == ""

    def test_tag_display_nothing_when_hide_marketing_in_context(self, issue, active_header_block):
        # GIVEN
        template = "{% load marketing_blocks %}{% render_marketing_block obj 'header' %}"

        # WHEN
        out = Template(template).render(Context({"hide_marketing": True, "obj": issue}))

        # THEN
        assert out == ""
