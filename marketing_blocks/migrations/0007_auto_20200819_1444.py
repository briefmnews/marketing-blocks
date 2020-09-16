# Generated by Django 2.2.15 on 2020-08-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing_blocks', '0006_auto_20191229_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingblock',
            name='position',
            field=models.CharField(choices=[('pre_header', 'pre_header'), ('header', 'header'), ('footer', 'footer'), ('pre_footer', 'pre_footer'), ('body_1', 'body_1'), ('body_2', 'body_2'), ('body_3', 'body_3'), ('body_4', 'body_4'), ('body_5', 'body_5')], default='header', max_length=10),
        ),
    ]