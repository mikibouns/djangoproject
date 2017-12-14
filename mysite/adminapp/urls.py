from django.conf.urls import url
import adminapp.views as admin_views

urlpatterns = [
    url(r'^users/create/$', admin_views.user_create, name='user_create'),
    url(r'^users/read/$', admin_views.users, name='users'),
    url(r'^users/update/(?P<pk>\d+)/$', admin_views.user_update, name='user_update'),
    url(r'^users/delete/(?P<pk>\d+)/$', admin_views.user_delete, name='user_delete'),

    url(r'^products/read/$', admin_views.ProductListView.as_view(), name='products'),
    url(r'^products/create/$', admin_views.products_create, name='products_create'),
    url(r'^products/update/(?P<pk>\d+)/$', admin_views.products_update, name='products_update'),
    url(r'^products/delete/(?P<pk>\d+)/$', admin_views.products_delete, name='products_delete'),
]
