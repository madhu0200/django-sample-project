"""signin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.views import View
#from python.pinternship.projects.envi.scripts.projects.signin.signin.settings import MEDIA_DIR, MEDIA_URL
from signin.views import *
from django.conf.urls import static
#from signin.view import use
urlpatterns = [
    path('registration/',registration,name='registration'),
    path('',home),
    path('admin/', admin.site.urls),
    path('register_user/',registeruser,name='register_user'),
    path('signin/',signin,name='signin'),
    path('show/',show,name='show'),
    path('showuser/',showuser,name='showuser'),
    path('signinuser/',signin,name='signinuser'),
    path('update/',update,name='update'),
    path('update_user/',updateUser,name='update_user'),
    path('deleteView/',deleteView,name='deleteView'),
    path('deleteViewUser/',deleteViewUser,name='deleteViewUser')
    
]
#urlpatterns= urlpatterns +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
