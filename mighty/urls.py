from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import redirect
from django.urls import include, path

from checker.views import home
from checker.urls import router as checker_router

urlpatterns = [
    url('app', home),
    url(r'^$', lambda request: redirect('app/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include(checker_router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
