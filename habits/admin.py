from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "place",
        "time",
        "action",
        "is_enjoyable",
        "related_habit",
        "periodicity",
        "reward",
        "duration",
        "is_public",
    )