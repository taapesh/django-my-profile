from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^about', views.about, name='about'),
    url(r'^projects', views.projects, name='projects'),
    url(r'^learn', views.learn, name='learn'),
]
