from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrator/', include('administrator.urls', namespace='administrator')),
    path('blog/', include('blog.urls', namespace='blog'))
]
