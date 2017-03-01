from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^step4$', views.step4),
    url(r'^step5$', views.step5),
]
