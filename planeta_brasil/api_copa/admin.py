#coding: utf-8
from django.contrib import admin
from .models import Country, City, Stadium, Match, News, Photo, Video


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class CityAdmin(admin.ModelAdmin):
    inlines = [ PhotoInline, ]

admin.site.register(City, CityAdmin)


class StadiumAdmin(admin.ModelAdmin):
	inlines = [ PhotoInline, ]

admin.site.register(Stadium, StadiumAdmin)


class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)


class MatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Match, MatchAdmin)


class NewsAdmin(admin.ModelAdmin):
    inlines = [ PhotoInline, ]

admin.site.register(News, NewsAdmin)


class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video)