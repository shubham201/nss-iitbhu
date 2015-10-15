from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /nss_app/
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^result/$', views.result, name="result"),
    url(r'^input/$', views.thank, name="index"),
    url(r'^add_volunteer/$', views.add_volunteer, name='add_volunteer'),
	url(r'^volunteer/(?P<volunteer_name_slug>[\w\-]+)/$', views.volunteer, name='volunteer'),
    url(r'^village/(?P<village_name_slug>[\w\-]+)/$', views.village, name='village'),
    url(r'^camp/(?P<camp_name_slug>[\w\-]+)/$', views.camp, name='camp'),
    url(r'^family/(?P<family_name_slug>[\w\-]+)/$', views.family, name='family'),
    url(r'^fund/(?P<fund_name_slug>[\w\-]+)/$', views.fund, name='fund'),

]