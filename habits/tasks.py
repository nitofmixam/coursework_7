from datetime import datetime, timedelta

import pytz

from celery import shared_task

from config import settings
from habits.services import send_telegram_message
from habits.models import Habit


@shared_task
def send_reminder_of_telegram():
    """Задача для отправки напоминания в Telegram."""
    periodicity = ["Раз в день", "Раз в два дня", "Раз в три дня", "Раз в четыре дня", "Раз в пять дней",
                   "Раз в шесть дней", "Раз в неделю"]
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    habits = Habit.objects.filter(is_enjoyable=False)

    for habit in habits:
        chat_id = habit.owner.tg_id
        message = f"Я буду {habit.action} в {habit.time} в {habit.place} "
        if habit.date_time <= current_datetime:
            send_telegram_message(chat_id, message)
            if habit.periodicity == periodicity[0]:
                habit.date_time = current_datetime + timedelta(days=1)
            elif habit.periodicity == periodicity[1]:
                habit.date_time = current_datetime + timedelta(days=2)
            elif habit.periodicity == periodicity[2]:
                habit.date_time = current_datetime + timedelta(days=3)
            elif habit.periodicity == periodicity[3]:
                habit.date_time = current_datetime + timedelta(days=4)
            elif habit.periodicity == periodicity[4]:
                habit.date_time = current_datetime + timedelta(days=5)
            elif habit.periodicity == periodicity[5]:
                habit.date_time = current_datetime + timedelta(days=6)
            elif habit.periodicity == periodicity[6]:
                habit.date_time = current_datetime + timedelta(days=7)
            habit.save()