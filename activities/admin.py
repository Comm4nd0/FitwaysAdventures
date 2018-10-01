from django.contrib import admin
from.models import Activity, Date
# Register your models here.


class ActivityAdminInLine(admin.TabularInline):
    model = Date
    extra = 3


class ActivityAdmin(admin.ModelAdmin):
    inlines = [ActivityAdminInLine, ]


class TrekAdmin(admin.ModelAdmin):
    pass


class TrainingAdmin(admin.ModelAdmin):
    pass


class ChallengeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Activity, ActivityAdmin)
