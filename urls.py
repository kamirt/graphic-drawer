from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'getgraphic', views.UploadViewSet)


urlpatterns = [
    url(r'^$', views.upload_file),
    url(r'^xlsread/$', views.readfile),
    url(r'^', include(router.urls)),
    url(r'^get/', include('rest_framework.urls', namespace='rest_framework'))
]