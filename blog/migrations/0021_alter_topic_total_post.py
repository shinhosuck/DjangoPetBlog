# Generated by Django 3.2 on 2023-12-29 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_topic_total_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='total_post',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
