from django.db import models

# Create your models here.


class Activity(models.Model):

    TYPE = (
        ('uk trip', 'UK Trip'),
        ('international trip', 'International Trip'),
        ('challenge', 'Challenge'),
        ('training', 'Training'),
    )

    type = models.CharField(choices=TYPE, default='UK Trip', max_length=250)

    title = models.CharField(max_length=250)
    image = models.ImageField(blank=True)
    map_image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    youtube_link = models.CharField(max_length=250, blank=True)

    price = models.CharField(blank=True, max_length=250)
    days = models.CharField(blank=True, max_length=250)
    daily_walking = models.CharField(blank=True, max_length=250)
    altitude = models.CharField(blank=True, max_length=250)

    GRADES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('hard', 'Hard'),
        ('very_hard', 'Very Hard'),
    )

    grade = models.CharField(choices=GRADES, default='Beginner', max_length=250)

    itinerary = models.TextField(blank=True)
    included = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)
    kit_list = models.TextField(blank=True)

    def __str__(self):
        return self.title



class Date(models.Model):
    title = models.ForeignKey(Activity, related_name='date', on_delete=models.PROTECT)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return str(self.title)
