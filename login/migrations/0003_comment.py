# Generated by Django 2.1.5 on 2019-03-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190219_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_title', models.CharField(default='', max_length=200)),
                ('comment_description', models.TextField(null=True)),
                ('rating', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
    ]
