# Generated by Django 2.1.5 on 2019-03-03 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_remove_comment_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
