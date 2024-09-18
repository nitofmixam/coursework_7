from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (DurationValidator, EnjoyableHabitValidator, RelatedHabitIsEnjoyableValidator,
                               RelatedHabitOrRewardValidator)


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RelatedHabitOrRewardValidator(field_1="related_habit", field_2="reward"),
            DurationValidator(field="duration"),
            EnjoyableHabitValidator(),
            RelatedHabitIsEnjoyableValidator(
                field_1="is_enjoyable", field_2="related_habit", field_3="reward"
            ),
        ]
