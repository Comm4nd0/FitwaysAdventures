from django.db import models

# Create your models here.

class Activities(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(blank=True)
    map_image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    youtube_link = models.CharField(max_length=250, blank=True)

    price = models.CharField(blank=True)
    days = models.CharField(blank=True)
    daily_walking = models.CharField(blank=True)
    altitude = models.CharField(blank=True)

    GRADES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('hard', 'Hard'),
        ('very_hard', 'Very Hard'),
    )

    grade = models.CharField(choices=GRADES, default='Beginner')

    itinerary = models.TextField(blank=True)
    included = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)
    kit_list = models.TextField(blank=True)

class Trek(models.Model)
    title = models.ForeignKey(Activities, on_delete=models.PROTECT)
    from_date = models.DateField()
    to_date = models.DateField()

class Challenge(models.Model)
    title = models.ForeignKey(Activities, on_delete=models.PROTECT)
    from_date = models.DateField()
    to_date = models.DateField()

class Training(models.Model)
    title = models.ForeignKey(Activities, on_delete=models.PROTECT)
    from_date = models.DateField()
    to_date = models.DateField()