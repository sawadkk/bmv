# Generated by Django 3.1.2 on 2021-09-26 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.TextField(max_length=50)),
                ('seating_capacity', models.IntegerField()),
                ('entry_fee', models.IntegerField()),
                ('screen_status', multiselectfield.db.fields.MultiSelectField(choices=[('empty', 'empty'), ('housefull', 'housefull'), ('filling', 'filling'), ('canceled', 'canceled')], max_length=32)),
                ('show_time', multiselectfield.db.fields.MultiSelectField(choices=[(1, '6am'), (2, '9am'), (3, '11am'), (4, '2pm'), (5, '5pm'), (6, '9pm')], max_length=11)),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.TextField()),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('play_time', models.DateTimeField()),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.screen')),
            ],
        ),
    ]
