from django.urls import path, include
from api import views
from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewset)
router.register(r'events', views.EventViewset)
router.register(r'users', views.UserViewSet)
router.register(r'profile', views.UserProfileViewset)
router.register(r'members', views.MemberViewset)
router.register(r'comments', views.CommentViewset)
router.register(r'bets', views.BetViewset)


urlpatterns = [
     path('', include(router.urls)),
     path('authenticate/', views.CustomObtainAuthToken.as_view()),  
 
]

