from rest_framework import filters


class AnswerFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(
            id__icontains=request.data["search"]
            if "search" in request.data else ""
        )
