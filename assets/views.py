from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from assets import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from c13.api import *

@login_required
def AssetListView(request):

    #搜索功能
    if request.method == 'POST':
        assets = models.Asset.objects.all()
        infos = request.POST.get('ipnmb','')
        if infos:
            assets = assets.filter(Q(ip__icontains=infos) | Q(admin_user__name__icontains=infos))
            return render(request, 'assets/host_list.html',
                          {'contacts': assets},
                          )

    assets = models.Asset.objects.all().order_by('-ip')
    paginator = Paginator(assets, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'assets/host_list.html',
                  {'contacts': contacts},
                  )
@login_required
def AssetDetailView(request):
    asset_id = request.GET.get('id', '')
    assets = models.Asset.objects.all()
    if asset_id:
        assets = assets.filter(Q(id__contains=asset_id))

        return render(request, 'assets/host_detail.html',
                      {'assets':assets}
                      )
@login_required
def AssetDeleteView(request):
    asset_id = request.GET.get('id', '')
    if asset_id:
        models.Asset.objects.filter(id=asset_id).delete()

    if request.method == 'POST':
        asset_batch = request.GET.get('arg', '')
        asset_id_all = str(request.POST.get('asset_id_all', ''))

        if asset_batch:
            for asset_id in asset_id_all.split(','):
                asset = get_object_or_404(models.Asset, id=asset_id)
                asset.delete()

    return HttpResponseRedirect('/assets/asset')


def AssetCreateView(request):
    return render(request, 'assets/host_create.html')
