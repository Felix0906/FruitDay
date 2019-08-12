from django.conf.urls import url
from .views import *


urlpatterns = [
    url('^$', index_views),
    url('^index/$', index_views),
    url('^login/$', login_views),
    url('^register/$', register_views),
]

urlpatterns += [
    url(r'^more/$', more_views),
    url(r'^logout/$', logout_views),
]

urlpatterns += [
    url(r'^check_login/$', check_login),
    url(r'^check_phone/$', check_phone),
]
urlpatterns += [
    url(r'^get_banner/$', banner_views),
    url(r'^get_adv/$', adv_views),
    url(r'^get_goods/$', get_goods),
]
urlpatterns += [
    url(r'^cart/$', cart_views),
    url(r'^add_cart/$', add_cart),
    url(r'get_cart_goods/$', get_cart_goods),
    url(r'^delete_goods/$', delete_goods),
    url(r'^cart_count/$', cart_count)
]
