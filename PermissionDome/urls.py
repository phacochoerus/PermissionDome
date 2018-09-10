from django.contrib import admin
from django.urls import path,include
from User.students import studentViewSet
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from User import views
from User.myPermissions.permissionViewSet import getPermissionsList,setPermissions

studentRouter = routers.DefaultRouter()
studentRouter.register('', studentViewSet.studentViewSet)



urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
	path('api-token-refre/', refresh_jwt_token),
    path('admin/', admin.site.urls),
    path('studentsviewset/', include(studentRouter.urls)),

    path('getUserPermission/', views.getUserPermission),
    path('addGroupPermissions/', views.addGroupPermissions),
    path('judgeUserPermission/', views.judgeUserPermission),
    path('getPermissionsList/', getPermissionsList.as_view()),
    path('setPermissions/', setPermissions.as_view()),


]
