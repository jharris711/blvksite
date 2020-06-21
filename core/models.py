from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary.uploader


class Soundcloud(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    embed_src = models.URLField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.id}: {self.title}"


class Pic(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)


class About(models.Model):
    title = models.CharField(max_length=50)
    paragraph_one = models.TextField()
    paragraph_two = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Instagram(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    embed = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.title}"
