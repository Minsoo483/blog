from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    # 127.0.0.1:8000/
    path("", views.index),
    # 127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/blog/
    path('blog/', include('blog.urls'))
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
