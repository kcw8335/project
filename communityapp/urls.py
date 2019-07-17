from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.communityapp, name="communityapp"),
    path('notice/', views.notice, name="notice"),
    path('community/', views.community, name="community"),
    path('communitydetail/<int:community_id>', views.communitydetail, name="communitydetail"),

    path('community/write/', views.communitywrite, name="communitywrite"),
    path('community/create/', views.communitycreate, name="communitycreate"),

    path('community/edit/<int:community_id>', views.communityedit, name="communityedit"),
    path('community/delete/<int:community_id>', views.communitydelete, name="communitydelete"),

    path('commentadd/<int:community_id>', views.commentadd, name="commentadd"),

    path('commentedit/<int:comment_id>', views.commentedit, name="commentedit"),
    path('commentdelete/<int:comment_id>', views.commentdelete, name="commentdelete"),
]