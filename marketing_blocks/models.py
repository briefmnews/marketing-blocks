from model_utils import Choices
from model_utils.models import TimeStampedModel

from django.db import models

from .managers import MarketingBlocksManager


class MarketingBlock(TimeStampedModel):

    POSITIONS = Choices(
        "pre_header",
        "header",
        "footer",
        "pre_footer",
        "body_1",
        "body_2",
        "body_3",
        "body_4",
        "body_5",
        "body_6",
        "body_7",
        "body_8",
        "body_9",
        "body_10",
        "paywall",
    )

    title = models.CharField(max_length=200)
    content_mailchimp = models.TextField(
        blank=True, default="", verbose_name="Contenu pour Mailchimp"
    )
    content_sendgrid = models.TextField(
        blank=True, default="", verbose_name="Contenu pour SendGrid"
    )
    active = models.BooleanField(default=False)
    position = models.CharField(
        choices=POSITIONS, default=POSITIONS.header, max_length=10
    )
    label = models.CharField(max_length=100, default="", null=True, blank=True)

    objects = MarketingBlocksManager()

    class Meta:
        ordering = ["-active", "-modified"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.active:
            try:
                block = MarketingBlock.objects.get_active_block_for_position_and_label(
                    self.position, self.label
                )
                block.active = False
                block.save()
            except AttributeError:
                pass

        super().save(*args, **kwargs)
