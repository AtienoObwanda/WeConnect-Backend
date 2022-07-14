from rest_framework.permissions import BasePermission



class IsHotelAdminUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_owner)


class IsCustomerUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_client)
