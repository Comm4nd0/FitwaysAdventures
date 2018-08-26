from django.contrib import admin
from.models import Activity, Trek, Training, Challenge
# Register your models here.


class ActivityAdmin(admin.ModelAdmin):
    pass


class TrekAdmin(admin.ModelAdmin):
    pass


class TrainingAdmin(admin.ModelAdmin):
    pass


class ChallengeAdmin(admin.ModelAdmin):
    pass



admin.site.register(Activity, ActivityAdmin)

admin.site.register(Trek, TrekAdmin)

admin.site.register(Training, TrainingAdmin)

admin.site.register(Challenge, ChallengeAdmin)