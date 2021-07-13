from django.core.exceptions import PermissionDenied
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        
        #check to see if the request that was made by the user is in SAFE_METhods
        #SAFE_METHODS are get / list / retreieve it doesnt not allow user to create or delete

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
    def is_admin(self, request, view, obj):
        if request.user.is_Admin:
            return True
        raise PermissionDenied
