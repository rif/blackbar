from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class BlackbarProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')


class Photo(models.Model):
    user = models.ForeignKey(User)
    caption = models.TextField(max_length=300)
    src = models.ImageField(upload_to="photos")
    pub_date = models.DateTimeField(auto_now=True)
    __unicode__ = lambda self: self.caption

    def get_absolute_url():
        return ""