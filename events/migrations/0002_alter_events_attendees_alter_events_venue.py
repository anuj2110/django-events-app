# Generated by Django 4.2 on 2023-05-03 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='events.myclubuser'),
        ),
        migrations.AlterField(
            model_name='events',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue'),
        ),
    ]