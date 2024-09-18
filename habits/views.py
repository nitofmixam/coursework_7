from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitCreateAPIView(CreateAPIView):
    """Класс для создания новой привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Метод получения cоздателя(владельца) привычки."""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(ListAPIView):
    """Класс для получения списка привычек текущего пользователя."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Habit.objects.filter(owner=user)
        return Habit.objects.all()


class HabitIsPublicListAPIView(ListAPIView):
    """Класс для получения списка элементов, с признаком is_public"""

    serializer_class = HabitSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(RetrieveAPIView):
    """Класс для получения одной привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    """Класс для изменения привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    """Класс для удаления привычки."""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated & IsOwner]