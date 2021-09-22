import pytest

from .factories import MarketingBlocksFactory
from .models import Issue


@pytest.fixture
def active_header_block():
    return MarketingBlocksFactory(
        title="Active Header", content="<p>I'm an active header</p>", active=True, label="issue"
    )


@pytest.fixture
def active_footer_block():
    return MarketingBlocksFactory(
        title="Active Footer",
        content="<p>I'm an active footer</p>",
        active=True,
        position="footer",
        label="issue",
    )


@pytest.fixture
def issue():
    return Issue()
