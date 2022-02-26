from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('', include('post.urls')),
    path('session/', include('session.urls')),
    path('tinymce/', include('tinymce.urls')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
