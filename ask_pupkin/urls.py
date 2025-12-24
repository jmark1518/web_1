"""
URL configuration for ask_pupkin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

from app.views import hello_view, bye_view, hello_template_view, base, main_page, hot_questions, tag_questions, one_question, login_view, logout_view, signup_view, create_question, profile_edit_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('bye/', bye_view),
    path('hello-template/', hello_template_view),
    path('base/', base, name='base'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('ask/', create_question, name='new_q'),
    path('profile/', profile_edit_view, name='profile_edit'),
    path('', include('app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

