"""tuturn URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mysite import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index,name='Home'),
    path('directlogin/', views.IndexDirectLogin, name='directlogin'),
    path('home2/', views.Index2, name='Home2'),
    path('home3/', views.Index3, name='Home3'),
    path('tutordetail/',views.Tutordetail,name='tutordetail'),
    path('search-list/', views.SearchList, name='Searchlist'),
    path('search-list2/', views.SearchList2, name='Searchlist2'),
    path('blogdetail/', views.BlogDetail, name='BlogDetail'),
    path('bloggrid/', views.BlogGrid, name='BlogGrid'),
    path('howitworks/', views.HowItWorks, name='howitworks'),
    path('package/', views.Package, name='package'),
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('forgot/', views.Forgot, name='forgot'),
    path('personaldetail/', views.PersonalDetail, name='personal'),
    path('contactdetail/', views.ContactDetail, name='contact'),
    path('educationdetail/', views.EducationDetail, name='education'),
    path('subjectsteach/', views.SubjectsTeach, name='subjectteach'),
    path('mediagallary/', views.MediaGallary, name='mediagallary'),
              ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
