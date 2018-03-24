
from django.conf.urls import url
from assets import views

app_name = 'assets'


urlpatterns = [
    url(r'^asset/$', views.AssetListView, name='asset-list'),
    url(r'^asset/detail/$', views.AssetDetailView, name='asset_detail'),
    url(r'^asset/delete/$', views.AssetDeleteView, name='asset_delete'),
    url(r'^asset/create/$', views.AssetCreateView, name='asset_create'),

]
