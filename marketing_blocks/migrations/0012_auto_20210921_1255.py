# Generated by Django 2.2.24 on 2021-09-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketing_blocks", "0011_auto_20210909_1614"),
    ]

    operations = [
        migrations.RemoveField(model_name="marketingblock", name="content_mailchimp",),
        migrations.AddField(
            model_name="marketingblock",
            name="content",
            field=models.TextField(blank=True, default="", verbose_name="Contenu"),
        ),
    ]
