"""mynews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from newsapp import views
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib import admin 
# admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.news, name="news"),
    path('burtguuleh/', views.burtguuleh, name='burtguuleh'),
    path('burtguuleh2/', views.burtguuleh2, name='burtguuleh2'),
    path('send/<int:pk>/', views.send, name='send'),
    path('torf/<int:pk>/', views.torf, name='torf'),
    path('login/', views.login, name='login'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('news/', views.news, name='news'),
    path('news2/<int:id>/', views.news2, name='news2'),
    path('upload/', views.upload, name='upload'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
