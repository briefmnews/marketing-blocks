import pytest

from factories import MarketingBlocksFactory


@pytest.fixture
def active_header_block():
    return MarketingBlocksFactory(
        title='Active Header',
        content='I\'m an active header',
        active=True,
    )


@pytest.fixture
def active_footer_block():
    return MarketingBlocksFactory(
        title='Active Footer',
        content='I\'m an active footer',
        active=True,
        position='footer'
    )
