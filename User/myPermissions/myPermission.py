from rest_framework import permissions


def getPermStr(Slef,request):
    method = Slef.action
    if method == "retrieve":
        method = "get+"
    elif method == "list":
        method = "get"
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


    permStr = "User.Students.%s"%(url_name+"."+method)

    return permStr



class isUserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        permStr = getPermStr(view,request)
        return request.user.has_perm("User.%s"%permStr)