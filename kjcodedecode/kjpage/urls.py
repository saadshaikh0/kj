from django.urls import path,include,re_path
from . import views
urlpatterns=[path("",views.home,name="home"),
            path("code/",views.code,name="code"),
            path("postdata/",views.postdata,name="postdata"),
            path("mcq/",views.mcq,name="mcq"),]