from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^step1$', views.step1),
    url(r'^step2$', views.step2),
    url(r'^step3$', views.step3),
    url(r'^step4$', views.step4),
    url(r'^step5$', views.step5),
    url(r'^step6$', views.step6), 
]
