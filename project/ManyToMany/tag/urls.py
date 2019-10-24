from django.urls import path, include
from tag import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='Post')
router.register(r'tags', views.TagViewSet, base_name='Tag')


app_name='tag' #Needed to run tests

#This is your endpoint API
urlpatterns = [
    path('', include(router.urls)),
]