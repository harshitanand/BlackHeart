from django.conf.urls import patterns, include, url
from django.contrib import admin
from BlackHeart import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BlackHeart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^Features/', views.features, name='features'),
    url(r'^polaroid/', include('polaroid.urls')),
    url(r'^accounts/', include('registration.urls')),
)
