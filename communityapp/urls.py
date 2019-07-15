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
]