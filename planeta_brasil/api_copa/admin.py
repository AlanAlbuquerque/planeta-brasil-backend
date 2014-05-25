#coding: utf-8
from django.contrib import admin
from .models import News, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class PhotoAdmin(admin.ModelAdmin):
    pass#inlines = [ PhotoInline, ]

admin.site.register(Photo, PhotoAdmin)


class NewsAdmin(admin.ModelAdmin):
    pass#inlines = [ PhotoInline, ]

admin.site.register(News, NewsAdmin)




# class CityAdmin(admin.ModelAdmin):
#     inlines = [ PhotoInline, ]

# admin.site.register(City, CityAdmin)


# class StadiumAdmin(admin.ModelAdmin):
# 	inlines = [ PhotoInline, ]

# admin.site.register(Stadium, StadiumAdmin)


# class CountryAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Country, CountryAdmin)


# class MatchAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Match, MatchAdmin)




# class VideoAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Video)