# Generated by Django 3.1.2 on 2021-10-14 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theater', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pen'), ('Approved', 'App'), ('Rejected', 'Rej'), ('Cancelled-User', 'Can-U'), ('Cancelled-Theater', 'Can-T')], max_length=300)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.show')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
