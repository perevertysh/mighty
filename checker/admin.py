from django.contrib import admin
from .models import Answer, AnswerStatus


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_time',)
    exclude = ('id',)
    list_filter = ['status__name', 'created_time']
    search_fields = ['status__name', 'created_time']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AnswerStatus)
class AnswerStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name',)
    exclude = ('id',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
