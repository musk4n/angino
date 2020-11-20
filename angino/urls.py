"""angino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # add these to configure our home page (default view) and result web page
    path('', views.home, name='home'),
    path('predictor/', views.predictor, name='predictor'),
<<<<<<< HEAD
    path('result/', views.result, name='result'),
=======
    path('tutorial/', views.tutorial, name='tutorial'),    
    path('measures/', views.measures, name='measures'),  
    path('forum/', views.forum, name='forum'), 
    path('result/', views.result, name='result'), 
    



>>>>>>> 5120816a3ae37c38ce97e24d3b8c2981a3d62791
]
# home, predictor, tutorial, measures, forum 