from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from taggit.managers import TaggableManager
from imagekit.models import ImageSpec
from imagekit.processors import resize

import re

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
        [resize.SmartCrop(260, 260),],
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
    position = models.CharField(choices=POSITION_CHOICES, max_length=1, default="2")

    def __unicode__(self):
        return self.title

cleanregex = re.compile(r'<[^>]+>')

class Post(models.Model):
    title = models.CharField(max_length=255)
    formatted_title = models.CharField(max_length=255, blank=True, help_text='Use this if you want italics in your title, use &lt;em&gt;thing in italics&lt;/em&gt;')
    slug = models.SlugField(unique=True)
    header_image = models.ForeignKey(Image, blank=True, null=True)
    body = models.TextField(blank=True)
    read_more = models.TextField(blank=True)
    embeds = models.ManyToManyField(Embed, blank=True, null=True)
    author = models.ForeignKey(User)
    published = models.BooleanField()
    timestamp = models.DateTimeField()
    likes = models.IntegerField(editable=False, default=0)

    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post', [self.slug])

    def get_permalink(self):
        permalink = 'http://%s%s' % (Site.objects.get_current().domain, self.get_absolute_url())
        return permalink

    def tag_list(self):
        return ",".join([t.name for t in self.tags.all()])

    def clean_body(self):
        return cleanregex.sub('', self.body) 

    class Meta:
        ordering = ['-timestamp']
        permissions = (("publish_post", "Can publish post"),
                       ("view_all_posts", "Can view and edit all posts"),
                       )


class Feature(models.Model):
    title = models.CharField(max_length=100)
    post = models.ForeignKey(Post)
    image = models.ForeignKey(Image, blank=True, null=True)
    byline = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(blank=True)
    order = models.IntegerField(default=1)

    def __unicode__(self):
        return self.title

class AuthorProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='images', blank=True, null=True)
    bio = models.TextField(blank=True)

    profile_image = ImageSpec(
        [resize.SmartCrop(100, 100),],
        image_field='avatar',
        format='JPEG',
        options={'quality': 90}
        )

    def __unicode__(self):
        return self.user.username

class Link(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    contributor = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
