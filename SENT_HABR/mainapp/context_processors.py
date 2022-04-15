from articleapp.models import Section


def sections(request):
    sections_menu = Section.objects.all()
    return {
        'sections_menu': sections_menu,
    }