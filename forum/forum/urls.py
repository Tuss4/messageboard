from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'forum.views.main'),
	url(r'^cat/(\d+)/$', 'structure.views.view_cat'),
	url(r'^sub_cat/(\d+)/$', 'structure.views.view_subcat'),

	#Topic URLs
	url(r'^add_topic/(\d+)/$', 'structure.views.add_topic'),
	url(r'^topic/(\d+)/', 'structure.views.view_topic'),
	url(r'^edit_topic/(\d+)/$', 'structure.views.edit_topic'),

	#Post URLs
	url(r'^edit_post/(\d+)/$', 'structure.views.edit_post'),

	#Auth URLs
	url(r'^login/$', 'forum.views.login'),
	url(r'^logout/$', 'forum.views.logout'),
	url(r'^register/$', 'forum.views.register'),
	
	#Profile URLs
	url(r'^edit_profile/(\d+)/$','profiles.views.edit_profile'),
	url(r'^view_profile/(\d+)/$','profiles.views.view_profile'),
	url(r'^add_grav/(\d+)/$', 'avatar.views.add_grav'),
    # Examples:
    # url(r'^$', 'forum.views.home', name='home'),
    # url(r'^forum/', include('forum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
