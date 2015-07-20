from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import myapp
urlpatterns = patterns('',
    # Examples:
    url(r'^register/$', 'myapp.views.register', name='register'),
    url(r'^login/$', 'myapp.views.loginapp', name='loginapp'),
    url(r'^logout/$', 'myapp.views.logoutapp', name='logoutapp'),
    url(r'^add_details/$', 'myapp.views.add_details', name='add_success'),
    url(r'^add_question/$', 'myapp.views.add_question', name='add_question'),
    url(r'^$', 'myapp.views.home', name='home'),
    url(r'^view_profile/$', 'myapp.views.view_profile', name='view_profile'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)