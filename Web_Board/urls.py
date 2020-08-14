"""Web_Board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from backend.views import home, BoardView, PostView, CommentView

# from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^signup/$', accounts_views.signup, name='signup'),
    path('', home, name='home'),
    path(r'boards/<int:pk>/', PostView.as_view(), name='posts'),
    path(r'boards/<int:pk>/posts/<int:pid>', CommentView.as_view(), name='comments'),
    path('boards/', BoardView.as_view(), name='boards'),
    path('account/', include('accounts.urls', 'accounts_api')),
]
