from django.views.generic.simple import direct_to_template


def preview(request):
    return direct_to_template(request, 'django_markdown/preview.html')
