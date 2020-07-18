from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from .models import AnswerStatus, Answer


class AnswerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerStatus
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):

    created_time = serializers.DateTimeField(format="%d-%m-%y %H:%M:%S")

    status = AnswerStatusSerializer(
        required=False,
        label=_("Статус задачи"),
        read_only=True
    )

    class Meta:
        model = Answer
        fields = "__all__"
