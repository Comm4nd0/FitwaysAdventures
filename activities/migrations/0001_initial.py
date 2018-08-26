# Generated by Django 2.1 on 2018-08-24 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('map_image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(blank=True)),
                ('youtube_link', models.CharField(blank=True, max_length=250)),
                ('price', models.CharField(blank=True, max_length=250)),
                ('days', models.CharField(blank=True, max_length=250)),
                ('daily_walking', models.CharField(blank=True, max_length=250)),
                ('altitude', models.CharField(blank=True, max_length=250)),
                ('grade', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('hard', 'Hard'), ('very_hard', 'Very Hard')], default='Beginner', max_length=250)),
                ('itinerary', models.TextField(blank=True)),
                ('included', models.TextField(blank=True)),
                ('extra_info', models.TextField(blank=True)),
                ('kit_list', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='activities.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='activities.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='Trek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='activities.Activity')),
            ],
        ),
    ]
