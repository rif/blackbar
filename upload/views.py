from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to, ajax_request
from django.shortcuts import redirect, get_object_or_404
from django.template import Context, Template
from forms import PhotoForm
from models import Photo

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

@render_to('upload/edit.html')
def edit(request, id):
    photo = get_object_or_404(Photo, pk=id)
    return locals()

@ajax_request
def get_full_caption(request, id):
    photo = get_object_or_404(Photo, pk=id)
    t = Template('{{ caption|linebreaks }}')
    return {'caption': t.render(Context({"caption": photo.caption}))}
