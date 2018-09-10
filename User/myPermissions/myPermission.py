from rest_framework import permissions
from django.contrib.auth.models import Permission,Group
from django.shortcuts import get_object_or_404
def getPermStr(Slef,request):
    method = Slef.action
    if method == "retrieve":
        pass
    elif method == "list":
        pass
    elif method == "update":
        method = "put"
    elif method == "create":
        method = "post"
    elif method == "destroy":
        method = "delete"

    url = request.path
    url_list = url.split("/")
    try:
        int(url_list[-2])
        url_name = url_list[-3]
    except:
        url_name = url_list[-2]

    obj_perm = get_object_or_404(Permission,codename__icontains=method + "." + url_name)
    return obj_perm.codename



class isUserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        permStr = getPermStr(view,request)
        return request.user.has_perm(view.app_name[0]+"."+permStr)