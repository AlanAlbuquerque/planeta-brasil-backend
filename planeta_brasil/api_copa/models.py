#coding: utf-8
from django.db import models
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from constants import CITY_CHOICES


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
				'name': getattr(self, 'name_%s' % lang),
				'description': getattr(self, 'description_%s' % lang),
			}

	def get_field(self, field, lang=None):
		lang = 1 if lang is None else int(lang)
		
		if lang == 2:
			return getattr(self, field + '_en')
		
		if lang == 3:
			return getattr(self, field + '_es')
		
		return getattr(self, field + '_pt')



class Guess(TimeStampedModel):
	country = models.PositiveIntegerField()
	user_id = models.TextField(blank=True)
	city = models.CharField(choices=CITY_CHOICES, max_length=2, null=True, blank=True)
	lang = models.PositiveSmallIntegerField(default=1)



class Device(models.Model):
	os = models.CharField(max_length=10)
	state = models.CharField(max_length=2, null=True)
	push_key = models.TextField(blank=False)
	language = models.CharField(max_length=2, default = '1')



class News(MultLangContent):
	city = models.CharField(choices=CITY_CHOICES, max_length=2, null=True, blank=True)
	photo = models.ForeignKey('api_copa.Photo', null=True, related_name='news_photos', blank=True)

	def as_dict(self, lang=None):
		data = super(News, self).as_dict(lang)
		data['id'] = unicode(self.id)
		data['photo'] = self.photo.url
		#data['photos'] = [p.as_dict() for p in self.photo_set.all()]
		return data




class Photo(TimeStampedModel):
	photo = models.ImageField(upload_to='photos', blank=False)
	thumb = ImageSpecField(source='photo', processors=[ResizeToFill(210, 140)], format='JPEG', options={'quality': 60})
	full = ImageSpecField(source='photo', processors=[ResizeToFill(420, 280)], format='JPEG', options={'quality': 60})

	def as_dict(self, lang=None):
		data = super(Photo, self).as_dict(lang)
		data['id'] = unicode(self.id)
		data['photo'] = self.full.url
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
		data = super(Photo, self).as_dict(lang)
		data['id'] = unicode(self.id)
		data['photo'] = self.full.url
		data['thumb'] = self.thumb.url
		return data




# class Match(TimeStampedModel):
# 	city = models.ForeignKey('api_copa.City')


# class Video(MultLangContent):
# 	youtube_url = models.URLField()

# 	city = models.ForeignKey('api_copa.City')

# 	@property
# 	def video_id(self):
# 		if self.youtube_url:
# 			qs = video_url.split('?')
# 			return urlparse.parse_qs(qs[1])['v'][0]
# 		return None

# 	def video_thumb_small(self):
# 		if self._video_id:
# 			return "http://img.youtube.com/vi/%s/2.jpg" % self.video_id
# 		return ''

# 	def video_thumb_big(self):
# 		if self._video_id:
# 			return "http://img.youtube.com/vi/%s/0.jpg" % self.video_id
# 		return ''