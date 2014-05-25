#coding: utf-8
from django.db import models
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Guess(TimeStampedModel):
	country = models.PositiveIntegerField()


class Device(models.Model):
	os = models.CharField(max_length=10)
	state = models.CharField(max_length=2, default='BR')
	push_key = models.TextField(blank=False)
	language = models.CharField(max_length=2, default = '1')



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


class Photo(MultLangContent):
	photo = models.ImageField(upload_to='photos', blank=False)
	thumb = ImageSpecField(source='photo', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})
	
	stadium = models.ForeignKey('api_copa.Stadium', blank=True)
	news = models.ForeignKey('api_copa.News', blank=True)
	city = models.ForeignKey('api_copa.City', blank=True)

	def as_dict(self, lang=None):
		data = super(Photo, self).as_dict(lang)
		data['id'] = unicode(self.id)
		data['photo'] = self.photo.url
		data['thumb'] = self.thumb.url
		return data


class City(MultLangContent):
	state_name = models.TextField()
	state_code =  models.CharField(max_length=2)


class Match(TimeStampedModel):
	city = models.ForeignKey('api_copa.City')


class Country(MultLangContent):
	code = models.TextField(max_length=2)
	flag = models.ImageField(upload_to='country', blank=True)
	flag_thumb = ImageSpecField(source='flag', processors=[ResizeToFill(100, 50)], format='JPEG', options={'quality': 60})


class Stadium(MultLangContent):
	city = models.ForeignKey('api_copa.City')


class News(MultLangContent):
	city = models.ForeignKey('api_copa.City')

	def as_dict(self, lang=None):
		data = super(News, self).as_dict(lang)
		data['id'] = unicode(self.id)
		data['city'] = self.city.as_dict(lang)
		data['photos'] = [p.as_dict() for p in self.photo_set.all()]
		return data


class Video(MultLangContent):
	youtube_url = models.URLField()

	city = models.ForeignKey('api_copa.City')

	@property
	def video_id(self):
		if self.youtube_url:
			qs = video_url.split('?')
			return urlparse.parse_qs(qs[1])['v'][0]
		return None

	def video_thumb_small(self):
		if self._video_id:
			return "http://img.youtube.com/vi/%s/2.jpg" % self.video_id
		return ''

	def video_thumb_big(self):
		if self._video_id:
			return "http://img.youtube.com/vi/%s/0.jpg" % self.video_id
		return ''