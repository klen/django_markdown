from django.shortcuts import render_to_response
def home(request):
    from django.http import HttpResponse
    from .forms import CustomForm

    form = CustomForm(request.POST)
    return render_to_response('md/home.html', dict(form=form))
