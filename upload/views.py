from django.utils.translation import ugettext_lazy as _
from annoying.decorators import render_to


@render_to('upload/index.html')
def index(request):
    return locals()