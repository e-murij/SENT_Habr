from django import template

register = template.Library()


@register.filter(name='user_in_list')
def user_in_list(objects, user):
    print(user)
    print(objects)
    if user.is_authenticated and objects:
        return objects.filter(user=user).exists()
    return False
