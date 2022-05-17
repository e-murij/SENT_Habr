from django.shortcuts import get_object_or_404

from notificationapp.models import Notification


def get_all_unread_notifications_by_user(queryset, user_id):
    """Возвращает всe непрочитанные уведомления пользователя user_id, отсортированные по дате изменения"""
    return queryset.filter(user=user_id, read=False)


def get_all_read_notifications_by_user(queryset, user_id):
    """Возвращает всe прочитанные уведомления пользователя user_id, отсортированные по дате изменения"""
    return queryset.filter(user=user_id, read=True)


def create_notify(user, content_type, object_id):
    """Создает и сохраняет запись в таблице Notification"""
    notification = Notification(user=user,
                                content_type=content_type,
                                object_id=object_id
                                )
    notification.save()


def delete_notif_about_object(content_type, object_id):
    """Удаляет все записи в таблице Notification относящиеся к объекту (content_type, object_id)"""
    notify_objects = Notification.objects.filter(content_type=content_type, object_id=object_id)
    notify_objects.delete()


def mark_notify_as_read(notify_id):
    """Отмечает сообщение как прочитанное"""
    notification = get_object_or_404(Notification, pk=notify_id)
    notification.read = True
    notification.save(update_fields=['read'])
