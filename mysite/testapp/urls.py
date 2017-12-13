from django.conf.urls import url

import testapp.views as test_views

urlpatterns = [
    url(r'^(?P<collection_name>\w+)/$', test_views.ajax_test, name='test1')
]
