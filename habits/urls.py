from django.urls import path
from habits.apps import HabitsConfig

from habits.views import (
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView, HabitIsPublicListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("ispublic/", HabitIsPublicListAPIView.as_view(), name="habits_is_public"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
    ]