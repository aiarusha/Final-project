from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import View, TemplateView, ListView, DetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', DetailView.as_view(), name="register"),
    path('', include('myApp.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)