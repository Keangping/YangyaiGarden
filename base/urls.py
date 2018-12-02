from django.conf.urls import url
from . import views

app_name = 'base'

urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contactus/$', views.contactus, name='contactus'),
	url(r'^service/$', views.service, name='service'),
	url(r'^event/$', views.event, name='event'),
	url(r'^property/$', views.property, name='property'),
	url(r'^activity/$', views.activity, name='activity'),
	
]