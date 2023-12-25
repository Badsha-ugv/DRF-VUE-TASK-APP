
from django.contrib import admin
from django.urls import path,include 

from django.conf import settings 
from django.conf.urls.static import static 

from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),

    # documentation swagger-ui and schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/doc/", SpectacularSwaggerView.as_view(
url_name="schema"), name="swagger-ui"),

    # loacl 
    path('api/',include('tasks.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 

