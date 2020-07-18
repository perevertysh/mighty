from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import pagination
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters import rest_framework as df_filters

from .models import (AnswerStatus, Answer)
from .serializers import (AnswerStatusSerializer, AnswerSerializer)
from .filters import AnswerFilterBackend
from .tasks import push_answer, check_answer


def home(request):
    return render(request, 'main.html', {})


class AnswerStatusViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerStatusSerializer
    queryset = AnswerStatus.objects.all().order_by("name")
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,
                       df_filters.DjangoFilterBackend]
    filterset_fields = ('code',)


class AnswerViewSet(viewsets.ModelViewSet):
    pagination_class = pagination.PageNumberPagination
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all().order_by("-created_time")
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,
                       df_filters.DjangoFilterBackend, AnswerFilterBackend]
    search_fields = ('id', 'status__name',)
    ordering_fields = ('id', 'status', 'created_time')
    filterset_fields = ('status__code',)

    @action(detail=False, methods=["post"])
    def add_submission(self, request):
        return Response(push_answer(request.data["answer"]))
    
    @action(detail=False, methods=["post"])
    def check_submission(self, request):
        return Response(check_answer(request.data["id"]))
