from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

import mainapp.views as main_views


urlpatterns = [
    url(r'^(?P<collection_name>\w+)/$', main_views.product_page, name='product_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)