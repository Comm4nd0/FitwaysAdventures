# Generated by Django 2.1 on 2018-10-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20181002_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='email',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='facebook',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='linkedin',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='twitter',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
