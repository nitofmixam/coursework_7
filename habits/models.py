from datetime import datetime

from django.db import models

from config import settings

NULLABLE = {"null": True, "blank": True}


class Habit(models.Model):
    DAILY = "Раз в день"
    EVERY_TWO_DAYS = "Раз в два дня"
    EVERY_THREE_DAYS = "Раз в три дня"
    EVERY_FOUR_DAYS = "Раз в четыре дня"
    EVERY_FIVE_DAYS = "Раз в пять дней"
    EVERY_SIX_DAYS = "Раз в шесть дней"
    WEEKLY = "Раз в неделю"

    PERIOD_CHOICES = (
        (DAILY, "Раз в день"),
        (EVERY_TWO_DAYS, "Раз в два дня"),
        (EVERY_THREE_DAYS, "Раз в три дня"),
        (EVERY_FOUR_DAYS, "Раз в четыре дня"),
        (EVERY_FIVE_DAYS, "Раз в пять дней"),
        (EVERY_SIX_DAYS, "Раз в шесть дней"),
        (WEEKLY, "Раз в неделю"),
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name="Создатель(владелец) привычки", **NULLABLE)

    place = models.CharField(max_length=50, verbose_name="Место", **NULLABLE)
    time = models.TimeField(verbose_name="Время, когда необходимо выполнять привычку")
    date_time = models.DateTimeField(verbose_name="Время рассылки", auto_now_add=True, **NULLABLE)
    action = models.CharField(max_length=50, verbose_name="Действие")

    is_enjoyable = models.BooleanField(default=False, verbose_name="Признак приятной привычки")

    related_habit = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Связанная привычка",
                                      **NULLABLE, related_name="related_to_habit")

    periodicity = models.CharField(choices=PERIOD_CHOICES, default=DAILY, verbose_name="Периодичность")

    reward = models.CharField(max_length=50, verbose_name="Вознаграждение", **NULLABLE)

    duration = models.DurationField(default=None, verbose_name="Время на выполнение привычки", **NULLABLE)

    is_public = models.BooleanField(default=False, verbose_name="Признак публичности", **NULLABLE)

    def __str__(self) -> str:
        return f"Я буду {self.action} в {self.time} в {self.place} "

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"