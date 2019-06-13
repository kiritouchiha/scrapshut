
from django.contrib import admin
from django.urls import path
# from django.conf.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from data.views import output,adddata  

urlpatterns = [
    path('adddata/',adddata,name='scrapshut'),
    path('output/',output),
    path('admin/', admin.site.urls),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
