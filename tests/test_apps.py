# -*- coding: utf-8 -*-
import pytest

from marketing_blocks.apps import MarketingBlocksConfig

pytestmark = pytest.mark.django_db()


class TestMarketingBlocksConfig(object):
    def test_apps(self):
        assert 'marketing_blocks' in MarketingBlocksConfig.name
