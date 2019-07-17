from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Community, Notice, Comment
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
    community.user = request.user
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save()
    return redirect('/communityapp/communitydetail/' + str(community.id))

@login_required
def communityedit(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    if request.method == 'POST':
        community.title = request.POST['title']
        community.body = request.POST['body']
        community.pub_date = timezone.datetime.now()
        community.save()
        return redirect('/communityapp/communitydetail/' + str(community.id))
    return render(request, 'communityedit.html', {'community':community})

@login_required
def communitydelete(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    community.delete()
    return redirect('/communityapp/community/')


@login_required
def commentadd(request, community_id):
    if request.method == "POST":
        post = Community.objects.get(pk=community_id)
        comment = Comment()
        comment.user = request.user
        comment.body = request.POST['body']
        comment.post = post
        comment.save()
        return redirect('/communityapp/communitydetail/' + str(community_id))
    else:
        return HttpResponse("잘못된 접근입니다.")

@login_required
def commentedit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        comment.body = request.POST['body']
        comment.save()
        return redirect('/communityapp/communitydetail/' + str(comment.post.id))
    else:
        context = {'comment':comment}
        return render(request, 'commentedit.html', {'comment':comment})

@login_required
def commentdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.user:
        if request.method == "POST":
            post_id = comment.post.id
            comment.delete()
            return redirect('/communityapp/communitydetail/'+ str(post_id))
    return HttpResponse('잘못된 접근입니다.')