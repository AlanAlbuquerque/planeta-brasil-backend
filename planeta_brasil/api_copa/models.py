#coding: utf-8
from django.db import models
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from constants import CITY_CHOICES, GROUP_CHOICES, TYPE_MATCH_CHOICES
from model_utils.choices import Choices


class MultLangContent(TimeStampedModel):
    name_pt = models.TextField()
    name_en = models.TextField()
    name_es = models.TextField()

    description_pt = models.TextField()
    description_en = models.TextField()
    description_es = models.TextField()

    __unicode__ = lambda self: self.name_pt

    class Meta:
        abstract = True

    def as_dict(self, lang=None):
        lang = lang or 'pt'
        return {
            'name': self.get_field('name', lang),
            'description': self.get_field('description', lang)
        }

    def get_field(self, field, lang=None):
        lang = lang or 'pt'
        return getattr(self, '%s_%s' % (field, lang))


class Guess(TimeStampedModel):
    country = models.PositiveIntegerField()
    user_id = models.TextField(blank=True)
    city = models.CharField(choices=CITY_CHOICES, max_length=2, null=True, blank=True)
    lang = models.PositiveSmallIntegerField(default=1)


class Device(models.Model):
    os = models.CharField(max_length=10)
    state = models.CharField(max_length=2, null=True)
    push_key = models.TextField(blank=False)
    language = models.CharField(max_length=2, default='1')


class News(MultLangContent):
    city = models.CharField(choices=CITY_CHOICES, max_length=2, null=True, blank=True)
    photo = models.ForeignKey('api_copa.Photo', null=True, related_name='news_photos', blank=True)

    def as_dict(self, lang=None):
        data = super(News, self).as_dict(lang)
        data['id'] = unicode(self.id)
        data['day'] = self.created.strftime('%d/%m')
        data['title'] = self.get_field('name', lang)
        data['img'] = self.photo.photo.url
        data['photos'] = [p.as_dict() for p in self.photo_set.all()]
        return data


class CulturalProgramming(MultLangContent):
    city = models.CharField(choices=CITY_CHOICES, max_length=2, null=True, blank=True)
    photo = models.ForeignKey('api_copa.Photo', null=True, related_name='cultural_programming_photos', blank=True)

    def as_dict(self, lang=None):
            data = super(CulturalProgramming, self).as_dict(lang)
            data['id'] = unicode(self.id)
            data['title'] = self.get_field('name', lang)
            data['describ'] = self.get_field('description', lang)
            data['img'] = self.photo.photo.url
            return data


class Photo(TimeStampedModel):
    photo = models.ImageField(upload_to='photos', blank=False)
    thumb = ImageSpecField(source='photo', processors=[ResizeToFill(210, 140)], format='JPEG', options={'quality': 60})
    full = ImageSpecField(source='photo', processors=[ResizeToFill(420, 280)], format='JPEG', options={'quality': 60})

    def as_dict(self, lang=None):
        data = {}
        data['id'] = unicode(self.id)
        data['img'] = self.full.url
        data['thumb'] = self.thumb.url
        return data


class UserPhoto(TimeStampedModel):
    photo = models.ImageField(upload_to='user_photos', blank=False)
    thumb = ImageSpecField(source='photo', processors=[ResizeToFill(210, 140)], format='JPEG', options={'quality': 60})
    full = ImageSpecField(source='photo', processors=[ResizeToFill(420, 280)], format='JPEG', options={'quality': 60})

    user_id = models.TextField(blank=True)
    city = models.CharField(choices=CITY_CHOICES, max_length=2, null=True, blank=True)
    lang = models.PositiveSmallIntegerField(default=1)

    def as_dict(self, lang=None):
        data = {}
        data['id'] = unicode(self.id)
        data['img'] = self.full.url
        data['thumb'] = self.thumb.url
        return data


class Team(MultLangContent):
    img_app = models.CharField(max_length=50)
    abbr = models.CharField(max_length=3)


class Stadium(TimeStampedModel):
    name = models.CharField(max_length=50)
    city = models.CharField(choices=CITY_CHOICES, max_length=2, null=True, blank=True)

    __unicode__ = lambda x: x.name


class Match(TimeStampedModel):

    TYPE_MATCH = Choices(*TYPE_MATCH_CHOICES)

    city = models.CharField(choices=CITY_CHOICES, max_length=2, null=True, blank=True)
    team_home = models.ForeignKey('api_copa.Team', null=True, related_name='teams_home', blank=True)
    team_visited = models.ForeignKey('api_copa.Team', null=True, related_name='teams_visited', blank=True)
    stadium = models.ForeignKey('api_copa.Stadium', null=True, related_name='matches_stadium', blank=True)

    group = models.CharField(choices=GROUP_CHOICES, max_length=1, null=True, blank=True)
    type_match = models.PositiveSmallIntegerField(choices=TYPE_MATCH, max_length=1, default=TYPE_MATCH.amistoso)
    result_home = models.PositiveSmallIntegerField(default=0)
    result_visited = models.PositiveSmallIntegerField(default=0)

    day_match = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.city:
            self.city = self.stadium.city
        return super(Match, self).save(*args, **kwargs)


class Locals(MultLangContent):
    logo = ImageSpecField(source='photo', processors=[ResizeToFill(60, 60)], format='JPEG', options={'quality': 60})


class GuessMatch(TimeStampedModel):
    email = models.EmailField(max_length=80)
    name = models.CharField(max_length=50)
    match = models.ForeignKey('api_copa.Match', null=True, related_name='matches_guess', blank=True)

    result_home = models.PositiveSmallIntegerField(default=0)
    result_visited = models.PositiveSmallIntegerField(default=0)

    hit = models.BooleanField(default=False)


# class Video(MultLangContent):
#   youtube_url = models.URLField()

#   city = models.ForeignKey('api_copa.City')

#   @property
#   def video_id(self):
#       if self.youtube_url:
#           qs = video_url.split('?')
#           return urlparse.parse_qs(qs[1])['v'][0]
#       return None

#   def video_thumb_small(self):
#       if self._video_id:
#           return "http://img.youtube.com/vi/%s/2.jpg" % self.video_id
#       return ''

#   def video_thumb_big(self):
#       if self._video_id:
#           return "http://img.youtube.com/vi/%s/0.jpg" % self.video_id
#       return ''
