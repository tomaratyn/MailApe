from django.contrib import admin

from mailinglist.models import Message, MailingList, Subscriber

admin.site.register(Message)
admin.site.register(MailingList)
admin.site.register(Subscriber)
