
from django.conf.urls import url
from assets import views

app_name = 'assets'


urlpatterns = [
    url(r'^asset/$', views.AssetListView, name='asset-list'),
    url(r'^asset/detail/$', views.AssetDetailView, name='asset_detail'),

]
