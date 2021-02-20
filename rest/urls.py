"""rest URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('auth/',include(('authentication.urls', 'auth'), namespace='auth')),
    path('expenses/',include(('expenses.urls', 'expenses'), namespace='expenses')),
    path('income/',include(('income.urls', 'income'), namespace='income')),
    path('userstats/',include(('userstats.urls', 'userstats'), namespace='userstats')),
]

handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'