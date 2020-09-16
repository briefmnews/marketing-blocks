import pytest

from .factories import MarketingBlocksFactory


@pytest.fixture
def active_header_block():
    return MarketingBlocksFactory(
        title="Active Header",
        content_mailchimp="I'm an active header",
        content_sendgrid="I'm a header too",
        active=True,
    )


@pytest.fixture
def active_footer_block():
    return MarketingBlocksFactory(
        title="Active Footer",
        content_mailchimp="I'm an active footer",
        content_sendgrid="I'm an active footer too",
        active=True,
        position="footer",
    )
