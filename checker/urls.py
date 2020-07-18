
from rest_framework import routers

from .views import (AnswerStatusViewSet,
                    AnswerViewSet)

router = routers.DefaultRouter()

routes = [
    router.register(r'answer', AnswerViewSet, basename='answer'),
    router.register(r'status', AnswerStatusViewSet, basename='status')
]

urlpatterns = []
