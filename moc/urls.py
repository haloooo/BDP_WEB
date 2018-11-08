"""sf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from RtMonSys.views import view_homePage

urlpatterns = [
    url(r'^$',view_homePage.go_homePage),
    url(r'^go_home',view_homePage.go_homePage),
    url(r'^get_all_model',view_homePage.get_all_model),
    url(r'^echo_once', view_homePage.echo_once),
    url(r'^set_pause',view_homePage.set_pause),
    url(r'^set_stop',view_homePage.set_stop),
    url(r'^set_output',view_homePage.set_output),
    url(r'^go_output',view_homePage.go_output),
    url(r'^showDetail',view_homePage.showDetail)
]
