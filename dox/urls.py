from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('dox.views',
    
    (r'^carrier/$', redirect_to, { 'url': 'https://www.registerguard.com', 'permanent':True },),    
    (r'^(?P<url>.*)$', 'page'),
    
)