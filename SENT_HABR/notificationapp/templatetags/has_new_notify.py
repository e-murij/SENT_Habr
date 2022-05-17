from django import template

from notificationapp.models import Notification

register = template.Library()


@register.filter(name='has_new_notify')
def has_new_notify(user):
    notifications = Notification.objects.filter(user=user, read=False)
    if notifications.exists():
        return True
    return False
