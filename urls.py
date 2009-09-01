from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve
from unipath import FSPath as Path

from django.contrib import admin
admin.autodiscover()

if settings.DEBUG:
    urlpatterns = patterns('', 
        (r'^m/(?P<path>.*)$', serve, 
            {'document_root' : Path(__file__).parent.child("media")}),
    )
else:
    urlpatterns = patterns('',)

urlpatterns += patterns('',
    (r'^', include('athletics.urls')),
    (r'^admin/', include(admin.site.urls)),
    
)
