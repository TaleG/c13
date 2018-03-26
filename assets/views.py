from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from assets import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from assets.forms import *
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


@login_required
def AssetCreateView(request):

    af = AssetForm()
    if request.method == 'POST':
        af_post = AssetForm(request.POST)
        ip = request.POST.get('ip', '')
        hostname = request.POST.get('hostname', '')
        try:
            if Asset.objects.filter(hostname=hostname):
                error = u'该主机名 %s 已存在！' % hostname
                raise ServerError(error)
            if len(hostname) > 64:
                error = u'主机名长度不能超过64位！'
                raise ServerError(error)
        except ServerError:
            pass

        else:
            if af_post.is_valid():
                asset_save = af_post.save(commit=False)
                if not ip:
                    asset_save.ip = hostname

                asset_save.save()
                af_post.save_m2m()

                msg = u'主机 %s 添加成功' % hostname
                return HttpResponseRedirect('/assets/asset')
            else:
                esg = u'主机 %s 添加失败' % hostname


    return render(request, 'assets/host_create.html', locals())
