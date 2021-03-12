from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrator/', include('administrator.urls', namespace='administrator')),
    path('account/', include('account.urls', namespace='account')),
    path('lms/', include('lms.urls', namespace='lms')),
    path('blog/', include('blog.urls', namespace='blog'))
]
