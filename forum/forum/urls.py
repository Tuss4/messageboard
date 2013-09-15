from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'forum.views.main'),
	url(r'^sub_cat/(\d+)/$', 'structure.views.view_subcat'),
	url(r'^cat/(\d+)/$', 'structure.views.view_cat'),
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^forum/', include('forum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
