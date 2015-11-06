from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /nss_app/
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^result/$', views.result, name="result"),
    url(r'^add_volunteer/$', views.add_volunteer, name='add_volunteer'),
    url(r'^add_village/$', views.add_village, name='add_village'),
    url(r'^add_camp/$', views.add_camp, name='add_camp'),
    url(r'^add_family/$', views.add_family, name='add_family'),
    url(r'^add_fund/$', views.add_fund, name='add_fund'),
	url(r'^volunteer/(?P<volunteer_name_slug>[\w\-]+)/$', views.volunteer, name='volunteer'), #gopal6465152126
    url(r'^village/(?P<village_name_slug>[\w\-]+)/$', views.village, name='village'), #durgakundvaranasi
    #url(r'^camp/(?P<camp_name_slug>[\w\-]+)(?P<year>[\w\-]+)/$', views.camp, name='camp'), #medical-2015-01-01
    url(r'^camp/(?P<camp_name_slug>[-A-Za-z0-9_]+)/$', views.camp, name='camp'),
    #url(r'^family/(?P<family_name_slug>[\w\-]+)/$', views.family, name='family'), #rajendra-prasadsachidanand-modi
    url(r'^family/(?P<family_name_slug>[-A-Za-z0-9_]+)/$', views.family, name='family'),
    url(r'^fund/(?P<fund_name_slug>[\w\-]+)/$', views.fund, name='fund'), #sfasd2015-12-31
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),

]