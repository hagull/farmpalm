from django.urls import path, re_path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('gcg', views.GcgViewSet)
router.register('anode', views.AnodeViewSet)
app_name = 'test_app'

urlpatterns = [
    path('test_request/', views.test_request, name = 'test_request'),
    path('test_post/', views.test_post, name = 'test_post'),
    path('test_get/', views.test_get, name = 'test_get'),
    path('test_protocol/', views.test_protocol, name = 'test_protocol'),
    path('test_dict', views.test_dict, name = 'test_dict'),
    #path('test_cam', views.test_cam, name = 'test_cam'),
    path('test_index1', views.index1, name = 'index1'),
    path('test_index2', views.index2, name = 'index2'),
    # rest api 사용
    path('', include(router.urls)),

]