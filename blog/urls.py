from django.urls import path, include
from . import views
from user import views as user_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name='blog-about'),
    
    #path('blog/', include('blog.urls')),  # ✅ this line includes blog/urls.py

]


