"""cokolwiek URL Configuration

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
from django.contrib import admin
from apka.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home$', HomeView.as_view(), name="home"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^create_user$', CreateUserView.as_view(), name='create'),
    url(r'^profile$', ProfilView.as_view(), name='user'),
    url(r'^case$', CaseView.as_view(), name='cases'),
    url(r'^case_details/(?P<pk>(\d)+)', CaseDetailsView.as_view(), name='case'),
    url(r'^add_money$', AddMoneyView.as_view(), name='money'),
    url(r'^inventory$', InventoryView.as_view(), name='inventory'),
]
