from django.conf.urls import url
from django.conf.urls import include, url
from . import views


from .views import (
        post_delete,
        )

app_name = 'menu'
urlpatterns = [
    url(r'^$', views.viewmenu, name='viewmenu'),
    url(r'^(?P<menu_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<menu_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^post/$', views.post, name='update'),
    url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
    #new information here
    url(r'^new/$', views.specialviewmenu, name='specialviewmenu'),
    url(r'^postnew/$', views.specialpost, name='specialupdate'),
    url(r'^postnew/(?P<pk>\d+)/$', views.specialdetail, name='specialdetail'),
    url(r'^manager$', views.managerview, name='managerview'),
    #SUREVEY URLS
    url(r'^survey/$', views.viewsurvey, name='survey'),
    url(r'^surveynew/$', views.viewpost, name='surveyupdate'),
    url(r'^survey/(?P<question_id>[0-9]+)/$', views.viewdetail, name='surveydetail'),
]
