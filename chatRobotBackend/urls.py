from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fileshandler/',include('fileshandler.urls')),
    path('studenthandler/',include('studenthandler.urls')),
    path('teacherhandler/',include('teacherhandler.urls')),
    path('adminhandler/',include('administratorhandler.urls')),
    path('translationhandler/',include('translationhandler.urls')),
    path('qrcodehandler/',include('qrcodehandler.urls')),
    path('conversationhandler/',include('conversationhandler.urls')),
    path('charthandler/',include('charthandler.urls')),
    path('classroomhandler/', include('classroomhandler.urls')),
]

# only in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)