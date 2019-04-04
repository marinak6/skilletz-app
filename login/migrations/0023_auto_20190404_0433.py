# Generated by Django 2.1.5 on 2019-04-04 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0022_auto_20190404_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(help_text='Additional notes for this hour', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField(help_text='Index of day within week (Ex. Sun = 0, Mon = 1, ... Sat = 6)')),
                ('hour', models.PositiveSmallIntegerField(help_text='Index of hor within day (Ex. 12am = 0, 1am = 1, ... 11pm = 23)')),
                ('display_text', models.CharField(help_text='display string used in views', max_length=20)),
            ],
            options={
                'ordering': ('day', 'hour'),
            },
        ),
        migrations.AddField(
            model_name='availabilityentry',
            name='hour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Hour'),
        ),
        migrations.AddField(
            model_name='availabilityentry',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='availability',
            field=models.ManyToManyField(through='login.AvailabilityEntry', to='login.Hour'),
        ),
    ]
