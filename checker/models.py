import uuid

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    """Abstract class for models objects add and modify history"""

    created_time = models.DateTimeField(_("создано"), auto_now=True)
    modified_time = models.DateTimeField(_("модифицировано"), auto_now=True)

    class Meta:
        abstract = True


class AnswerStatus(models.Model):
    """Status of task"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
                            verbose_name="Название")
    code = models.CharField(max_length=256,
                            verbose_name="Код")

    def __str__(self):
        return self.name


class Answer(TimeStampedModel):
    """Task description"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    check_id = models.IntegerField(verbose_name=_("Идентификатор проверки"),
                                   null=True)

    answer = models.TextField(max_length=2000, verbose_name=_("Ответ"))

    status = models.ForeignKey("checker.AnswerStatus",
                               null=True, on_delete=models.SET_NULL,
                               verbose_name=_("Статус проверки"),
                               related_name=_("ANSWER_ANSWER_STATUS"))

    def __str__(self):
        return f"answer:{str(self.id)[0:8]}"

    def get_absolute_url(self):
        return reverse('answer-detail', kwargs={'pk': self.pk})
