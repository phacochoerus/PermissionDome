from rest_framework import viewsets
from User import models
from User.pagination import MyPageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.http import Http404
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from User.students import studentSerializer
from User.myPermissions import myPermission
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404,get_list_or_404

"""
获取权限
"""





class getPermissionsList(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    def get(self,request):
        queryset_perm = Permission.objects.filter(codename__icontains="User.")
        dict_perm = {}
        list_perm = []
        for foo in queryset_perm:
            name_list = foo.name.split(".")
            if name_list[0] not in dict_perm:
                dict_perm[name_list[0]] = {}
            if name_list[1] not in dict_perm[name_list[0]]:
                dict_perm[name_list[0]][name_list[1]] = []
            dict_perm[name_list[0]][name_list[1]].append(name_list[2])
        print(dict_perm)
        return Response({"code":status.HTTP_200_OK,"success":True,"msg":"权限列表","results":dict_perm},status=status.HTTP_200_OK)



class setPermissions(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    def post(self,request):
        dict_perm = request.data
        group = dict_perm["group"]
        obj_group = get_object_or_404(Group,name=group)
        for k,v in dict_perm["perm"]["User"].items():
            for k1,v1 in v.items():
                str = "User." + k + "." + k1
                obj_perm = Permission.objects.filter(name__icontains=str).first()
                if v1 == 1:
                    obj_group.permissions.add(obj_perm)
                else:
                    obj_group.permissions.remove(obj_perm)

        return Response({"code":status.HTTP_200_OK,"success":True,"msg":"修改权限成功","results":None},status=status.HTTP_200_OK)



