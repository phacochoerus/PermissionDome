from rest_framework import permissions


def getPermStr(Slef,request,view):
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

    permStr = view.perm_group[0] + "." + method + "." + url_name
    return permStr



class isUserPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        permStr = getPermStr(view,request,view)
        return request.user.has_perm("User.%s"%permStr)