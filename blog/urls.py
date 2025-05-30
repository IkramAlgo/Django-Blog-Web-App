from django.urls import path, include
from . import views
from user import views as user_views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/str:<username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name='blog-about'),
    path('logout/', user_views.logout_view, name='logout'),
    
    
    # path('blog/', include('blog.urls')),  # ✅ this line includes blog/urls.py

]


