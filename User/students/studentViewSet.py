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
from rest_framework import permissions
from django.urls import reverse


class studentViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,myPermission.isUserPermissions,)
    queryset = models.UserProfile.objects.all()
    serializer_class = studentSerializer.studentsSerializer
    pagination_class = MyPageNumberPagination
    app_name = ["User",]


    def initial(self, request, *args, **kwargs):
        self.format_kwarg = self.get_format_suffix(**kwargs)
        neg = self.perform_content_negotiation(request)
        request.accepted_renderer, request.accepted_media_type = neg
        version, scheme = self.determine_version(request, *args, **kwargs)
        request.version, request.versioning_scheme = version, scheme
        self.perform_authentication(request)
        self.check_permissions(request)
        self.check_throttles(request)

