from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from blackbar import settings
import os

class BlackbarProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')


class Photo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=75)
    caption = models.TextField()
    src = models.ImageField(upload_to="photos")
    pub_date = models.DateTimeField(auto_now=True)
    __unicode__ = lambda self: self.title

    def get_absolute_url():
        return ""

    def save(self, *args, **kwargs):
        import cv
        super(Photo, self).save(*args, **kwargs) # Call the "real" save() method.
        file_name = os.path.join(settings.MEDIA_ROOT, self.src.name)
        im = cv.LoadImage(file_name)#, cv.CV_LOAD_IMAGE_GRAYSCALE) # input image
        size = cv.GetSize(im)
	if size[0] > 1500 or size[1] > 1500:
                thumbnail = cv.CreateImage( ( int(size[0] / 2.5), int(size[1] / 2.5)), im.depth, im.nChannels)
                cv.Resize(im, thumbnail)
                im = thumbnail
        # loading the classifiers
        haarFace = cv.Load(os.path.join(settings.STATIC_ROOT, 'haarcascade_frontalface_default.xml'))
        haarEyes = cv.Load(os.path.join(settings.STATIC_ROOT, 'haarcascade_eye.xml'))
        # running the classifiers
        storage = cv.CreateMemStorage()
        detectedFace = cv.HaarDetectObjects(im, haarFace, storage)
        detectedEyes = cv.HaarDetectObjects(im, haarEyes, storage)

        # draw a green rectangle where the face is detected
        if detectedFace:
         for face in detectedFace:
          cv.Rectangle(im,(face[0][0],face[0][1]),
                       (face[0][0]+face[0][2],face[0][1]+face[0][3]),
                       cv.RGB(155, 255, 25),2)

        # draw a purple rectangle where the eye is detected
        if detectedEyes:
         for eye in detectedEyes:
          cv.Rectangle(im,(eye[0][0],eye[0][1]),
                           (eye[0][0]+eye[0][2],eye[0][1]+eye[0][3]),
                           cv.RGB(155, 55, 200),2)
        cv.SaveImage(file_name, im)

