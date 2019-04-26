import factory

from marketing_blocks.models import MarketingBlock


class MarketingBlocksFactory(factory.django.DjangoModelFactory):
    """MarketingBlocks factory"""

    class Meta:
        model = MarketingBlock
