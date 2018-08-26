# Generated by Django 2.1 on 2018-08-24 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('uk trip', 'UK Trip'), ('international trip', 'International Trip'), ('challenge', 'Challenge'), ('training', 'Training')], default='UK Trip', max_length=250),
        ),
    ]
