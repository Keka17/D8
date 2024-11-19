
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from News import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('News.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.IndexView.as_view(template_name='home.html')),
    path('upgrade/', views.upgrade_me, name='upgrade_me')
]

