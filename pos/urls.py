from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='order')),
    url(r'^order/$', views.order, name='order'),
    url(r'^addition/(?P<operation>[A-Za-z0-9\.\+\(\)\-\_ ]*)/?$', views.addition, name='addition'),
    url(r'^cash/(?P<amount>[0-9\.]*)/?$', views.cash, name='cash')
]
