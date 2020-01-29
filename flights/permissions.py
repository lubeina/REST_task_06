from datetime import date
from rest_framework.permissions import BasePermission

class IsBookingOwnerOrStaff(BasePermission):
	def has_object_permission(self,request,view,obj):
		if request.user.is_staff or request.user == obj.user:
			return True

		return False

class UpcomingBooking(BasePermission):
	def has_object_permission(self,request,view,obj):
		if (obj.date - date.today()).days > 3 :
			return True

		return False