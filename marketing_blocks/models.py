# -*- coding: utf# Create your models here.-8 -*-
from __future__ import unicode_literals

from model_utils import Choices
from model_utils.models import TimeStampedModel

from django.db import models

from .managers import MarketingBlocksManager


class MarketingBlock(TimeStampedModel):

    POSITIONS = Choices("header", "footer")

    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    position = models.CharField(
        choices=POSITIONS, default=POSITIONS.header, max_length=10
    )

    objects = MarketingBlocksManager()

    class Meta:
        ordering = ["-active", "-modified"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.active:
            try:
                block = MarketingBlock.objects.get_active_block_for_position(
                    self.position
                )
                block.active = False
                block.save()
            except AttributeError:
                pass

        super(MarketingBlock, self).save(*args, **kwargs)
