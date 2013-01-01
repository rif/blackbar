from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to
from django.shortcuts import redirect
from forms import PhotoForm

@login_required
@render_to('upload/upload.html')
def upload(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_photo = form.save(commit=False)
        new_photo.user = request.user
        new_photo.save()
        return redirect('index')
    return locals()