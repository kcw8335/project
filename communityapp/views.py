from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Community, Notice
from django.contrib.auth.decorators import login_required

def communityapp(request):
    return render(request, 'communityapp.html')

def notice(request):
    notices = Notice.objects
    return render(request, 'notice.html', {'notices':notices})

def community(request):
    communities = Community.objects
    communities_list = Community.objects.all()
    paginator = Paginator(communities_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'community.html', {'communities':communities, 'posts':posts})

def communitydetail(request, community_id):
    communitydetail = get_object_or_404(Community, pk=community_id)
    return render(request, 'communitydetail.html', {'communitydetail':communitydetail})

@login_required
def communitywrite(request):
    return render(request, 'communitywrite.html')

@login_required
def communitycreate(request):
    community = Community()
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save()
    return redirect('/communityapp/communitydetail/' + str(community.id))