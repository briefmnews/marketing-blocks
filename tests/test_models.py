import pytest

from .factories import MarketingBlocksFactory

pytestmark = pytest.mark.django_db(transaction=True)


class TestMarketingBlock(object):
    def test_custom_save(self, active_header_block):
        """Custom save method should allow only one active block by position"""

        # GIVEN
        assert active_header_block.active

        # WHEN
        second_block = MarketingBlocksFactory(
            title="Title 2", content="bla 2", active=True, position="header"
        )
        assert second_block.active

        # THEN
        active_header_block.refresh_from_db()
        assert not active_header_block.active

    def test_unicode(self, active_header_block):
        """Unicode should return the block's title"""
        # WHEN
        unicode_title = active_header_block.__unicode__()

        # THEN
        assert unicode_title == active_header_block.title
