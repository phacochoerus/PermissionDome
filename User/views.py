from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib.auth.models import Permission,Group
from User import models
from django.urls import reverse,resolve
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

def getUserPermission(request):
    print(dir(request.META))
    print(request.META)
    obj_user = get_object_or_404(models.UserProfile,username="student1")
    # print(obj_user.user_permissions.all()) # 获取user的所有权限
    return HttpResponse("拿到用户所有的权限")

def judgeUserPermission(request):
    obj_user = get_object_or_404(models.UserProfile,username="student1")
    has = obj_user.has_perm("User.User.Students.studentsviewset.post")
    print(has)
    return HttpResponse("判断user是否有某个权限:%s"%has)

def addGroupPermissions(request):
    obj_group = get_object_or_404(Group,name="student")
    print(obj_group)
    obj_perm = get_object_or_404(Permission,codename="User.Students.studentsviewset.post")
    print(obj_perm)
    obj_group.permissions.add(obj_perm)
    return HttpResponse("给用户组添加权限")


class judgeGroupPermission(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    def post(self,request):
        obj_group = get_object_or_404(Group,name=request.data["name"])
        queryset_group = obj_group.permissions.all()
        print(obj_group.permissions.all())
        print(dir(obj_group))
        obj_perm = Permission.objects.get(codename="User.Students.create.studentsviewset")
        if obj_perm in queryset_group:
            print("在")
        else:
            print("No")


        return HttpResponse("判断user是否有某个权限:%s")
