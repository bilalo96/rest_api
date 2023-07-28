from django.urls import path,include # to include list of view in urlpatterns and assigned a list to specific url
from rest_framework.routers import DefaultRouter
from profiles_api import views


router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, basename='hello-viewset')
router.register('profile',views.UserProfileViewSet)#we don't need to pass base_name like hello_viewset because we have queryset in views

urlpatterns=[
   path('hello-view/',views.HelloApiView.as_view()),
   path('',include(router.urls))#when register new routers with our route it generate alist of URLs that assosiated for our views
    # '' because we don't want to put a prefix to this url we just want to include all of the urls in  the base of this URLs file
]
