from django.shortcuts import render


def preview(request):
    return render(
            request, 'django_markdown/preview.html',
            content=request.REQUEST.get('data', 'No content posted'))
