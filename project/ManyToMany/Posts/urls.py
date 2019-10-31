from django.urls import path, include
from Posts import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, base_name='Post')



app_name='Posts' #Needed to run tests

#This is your endpoint API
urlpatterns = [
    path('', include(router.urls)),
]