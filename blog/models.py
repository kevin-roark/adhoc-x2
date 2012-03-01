from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from imagekit.models import ImageSpec
from imagekit.processors import resize

from music.models import MusicEmbed

class Image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images')
    caption = models.TextField(blank=True)
    medium_image = ImageSpec(
        [resize.Fit(580, 1080),],
        image_field='image',
        format='JPEG', 
        options={'quality': 90}
        )
    feature_image = ImageSpec(
        [resize.Fit(250, 250),],
        image_field='image',
        format='JPEG',
        options={'quality': 90}
        )

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.title:
            self.title = self.image.name

        super(Image, self).save()


class Embed(models.Model):
    POSITION_CHOICES = (
        ('1', 'Top'),
        ('2', 'Above Read More'),
        ('3', 'Below Read More'),
        ('4', 'Bottom'),
        )
    title = models.CharField(max_length=255)
    body = models.TextField(help_text="Either a url or embed code", blank=True)
    music_embed = models.ForeignKey(MusicEmbed, blank=True, null=True)
    position = models.CharField(choices=POSITION_CHOICES, max_length=1, default="4")

    def __unicode__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    header_image = models.ForeignKey(Image, blank=True, null=True)
    body = models.TextField(blank=True)
    read_more = models.TextField(blank=True)
    embeds = models.ManyToManyField(Embed, blank=True, null=True)
    author = models.ForeignKey(User)
    published = models.BooleanField(default=True)
    timestamp = models.DateTimeField()

    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post', [self.slug])

class Feature(models.Model):
    title = models.CharField(max_length=100)
    post = models.ForeignKey(Post)
    image = models.ForeignKey(Image, blank=True, null=True)
    byline = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(blank=True)
    order = models.IntegerField(default=1)
