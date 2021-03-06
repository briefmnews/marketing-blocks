# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-23 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketing_blocks", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="marketingblock",
            options={"ordering": ["-active", "-modified"]},
        ),
        migrations.AlterField(
            model_name="marketingblock",
            name="position",
            field=models.CharField(
                choices=[
                    ("header", "header"),
                    ("footer", "footer"),
                    ("pre_footer", "pre_footer"),
                    ("body_1", "body_1"),
                    ("body_2", "body_2"),
                    ("body_3", "body_3"),
                    ("body_4", "body_4"),
                    ("body_5", "body_5"),
                ],
                default="header",
                max_length=10,
            ),
        ),
    ]
