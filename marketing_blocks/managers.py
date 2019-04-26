from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class MarketingBlocksManager(models.Manager):

    def get_active_block_for_position(self, position):
        """Returns the active block for a specific position"""
        try:
            block = self.get(position=position, active=True)
        except ObjectDoesNotExist:
            block = None

        return block

    def get_block_contents_by_position(self):
        """Returns all the active block contents by position"""

        blocks = self.filter(active=True)

        data = {block.position: block.content for block in blocks}

        return data
