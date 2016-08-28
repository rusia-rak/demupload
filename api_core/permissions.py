from rest_framework.permissions import SAFE_METHODS 
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
	'''
	Custom permissions class 
	
	Provides Read Only Access to GET, HEAD, OPTIONS requests

	Admin access to POST, PUT, PATCH & DELETE
	'''
	def has_permission(self, request, view):

		if request.method in SAFE_METHODS:
			return True
		else:
			return request.user and request.user.is_staff