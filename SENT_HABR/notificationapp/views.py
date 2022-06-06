from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView

from notificationapp.models import Notification
from notificationapp.services import mark_notify_as_read, \
    get_all_unread_notifications_by_user, get_all_read_notifications_by_user


class NotificationsList(LoginRequiredMixin, ListView):
    """Вывод списка уведомлений для залогиненного пользователя"""
    template_name = 'notificationapp/my_notifications.html'
    model = Notification

    def get_context_data(self, **kwargs):
        context = super(NotificationsList, self).get_context_data(**kwargs)
        context['unread_notify'] = get_all_unread_notifications_by_user(self.get_queryset(), self.request.user.pk)
        context['read_notify'] = get_all_read_notifications_by_user(self.get_queryset(), self.request.user.pk)
        context['title'] = 'My Notifications'
        return context


class MarkAsRead(LoginRequiredMixin, View):
    """Отметить уведомление как прочитанное"""
    def get(self, request, pk):
        mark_notify_as_read(pk)
        return redirect(request.META.get('HTTP_REFERER'))
