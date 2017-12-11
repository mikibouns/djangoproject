from django.conf.urls import url
import adminapp.views as admin_views

urlpatterns = [
    url(r'^users/create/$', admin_views.user_create, name='user_create'),
    url(r'^users/read/$', admin_views.UsersListView.as_view(), name='users'),
    url(r'^users/update/(?P<pk>\d+)/$', admin_views.user_update, name='user_update'),
    url(r'^users/delete/(?P<pk>\d+)/$', admin_views.user_delete, name='user_delete'),
]
