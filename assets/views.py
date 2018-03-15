from django.shortcuts import render
from assets import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def AssetListView(request):

    #搜索功能
    if request.method == 'POST':
        assets = models.Asset.objects.all()
        infos = request.POST.get('ipnmb','')
        if infos:
            assets = assets.filter(Q(ip__icontains=infos) | Q(admin_user__name__icontains=infos))
            return render(request, 'assets/hosts.html',
                          {'contacts': assets},
                          )

    assets = models.Asset.objects.all().order_by('-ip')
    paginator = Paginator(assets, 1)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'assets/hosts.html',
                  {'contacts': contacts},
                  )