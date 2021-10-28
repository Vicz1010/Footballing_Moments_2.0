from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('chelsea/',views.ChelseaView.as_view(), name='chelsea'),
    path('inter/',views.InterView.as_view(), name='inter'),
    path('spain/',views.SpainView.as_view(), name='spain'),
    path('thread/',views.ThreadListView.as_view(),name='thread_list'),
    path('thread/<int:pk>', views.ThreadDetailView.as_view(), name='thread_detail'),
    path('thread/new/', views.ThreadCreateView.as_view(), name='thread_new'),
    path('thread/<int:pk>/edit', views.ThreadUpdateView.as_view(), name='thread_edit'),
    path('thread/<int:pk>/remove', views.ThreadDeleteView.as_view(), name='thread_remove'),
    path('accounts/signup/', views.sign_up, name='sign_up'),
    path('comments/<int:pk>/comment', views.add_comment_to_thread, name='add_comment_to_thread'),
    path('comments/<int:pk>/approve', views.approve_comment, name='approve_comment'),
    path('comments/<int:pk>/remove', views.remove_comment, name='remove_comment'),
]