# Generated by Django 3.2 on 2023-12-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_topic_topic_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
