from rest_framework.permissions import BasePermission

from mailinglist.models import Subscriber, MailingList


class CanUseMailingList(BasePermission):

    message = 'User does not have access to this resource.'

    def has_object_permission(self, request, view, obj):
        user = request.user
        if isinstance(obj, Subscriber):
            return obj.mailing_list.user_can_use_mailing_list(user)
        elif isinstance(obj, MailingList):
            return obj.user_can_use_mailing_list(user)
        return False
