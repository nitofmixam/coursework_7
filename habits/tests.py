from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование привычек."""
    def setUp(self) -> None:
        self.user = User.objects.create(email="test@test.ru")
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создания привычки."""
        data = {
            "time": "17:00",
            "action": "test",
            "place": "test"
        }
        response = self.client.post(
            "/habits/create/",
            data=data
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            out_data.get("place"),
            "test")

        self.assertEqual(
            out_data.get("time"),
            "17:00:00")

        self.assertEqual(
            out_data.get("action"),
            "test")

        self.assertEqual(
            out_data.get("periodicity"),
            "Раз в день")

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habits(self):
        """Тестирование вывода списка привычек текущего пользователя."""

        Habit.objects.create(
            time="17:00",
            action="test",
            place="test",
            owner=self.user
        )

        response = self.client.get(
            "/habits/"
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.json()),
            4
        )

        self.assertEqual(
            out_data["results"][0].get("place"),
            "test")

        #Для наставника
        # self.assertEqual(
        #     out_data["results"][0].get("owner"),
        #     1)

        #Для меня
        # self.assertEqual(
        #     out_data["results"][0].get("owner"),
        #     3)

    def test_retrieve_habit(self):
        """Тестирование вывода привычки"""

        habit = Habit.objects.create(
            time="17:00",
            action="test",
            place="test",
            owner=self.user
        )

        response = self.client.get(
            f"/habits/{habit.id}/"
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            out_data.get("place"),
            "test")

        self.assertEqual(
            out_data.get("time"),
            "17:00:00")

        self.assertEqual(
            out_data.get("action"),
            "test")

        self.assertEqual(
            out_data.get("periodicity"),
            "Раз в день")

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_is_public_habits(self):
        """Тестирование вывода списка привычек текущего пользователя."""

        Habit.objects.create(
            time="17:00",
            action="test",
            place="test",
            owner=self.user,
            is_public=True
        )

        response = self.client.get(
            "/habits/ispublic/"
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.json()),
            1
        )

        self.assertEqual(
            out_data[0].get("place"),
            "test")

        self.assertEqual(
            out_data[0].get("is_public"),
            True)

    def test_update_habit(self):
        """Тестирование обновления привычки"""

        habit = Habit.objects.create(
            time="17:00",
            action="before update test",
            place="before update test",
            owner=self.user
        )

        data = {
            "time": "18:00",
            "action": "after update test",
            "place": "after update test"
        }

        response = self.client.patch(
            f"/habits/{habit.id}/update/",
            data
        )

        # print(response.json())

        out_data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            out_data.get("time"),
            "18:00:00")

        self.assertEqual(
            out_data.get("place"),
            "after update test")

        self.assertEqual(
            out_data.get("action"),
            "after update test")

        self.assertEqual(
            out_data.get("periodicity"),
            "Раз в день")

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_delete_habit(self):
        """Тестирование удаления привычки"""

        habit = Habit.objects.create(
            time="17:00",
            action="before update test",
            place="before update test",
            owner=self.user
        )

        response = self.client.delete(
            f"/habits/{habit.id}/delete/"
        )

        # print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Habit.objects.all().exists()
        )