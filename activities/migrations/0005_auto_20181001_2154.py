# Generated by Django 2.1 on 2018-10-01 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20181001_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dates', to='activities.Activity'),
        ),
    ]