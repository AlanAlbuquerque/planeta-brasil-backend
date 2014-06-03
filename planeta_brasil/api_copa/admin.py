#coding: utf-8
from django.contrib import admin
from .models import *


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

class PhotoAdmin(admin.ModelAdmin):
    pass#inlines = [ PhotoInline, ]

admin.site.register(Photo, PhotoAdmin)

class NewsAdmin(admin.ModelAdmin):
    pass#inlines = [ PhotoInline, ]

admin.site.register(News, NewsAdmin)

class StadiumAdmin(admin.ModelAdmin):
	inlines = [ PhotoInline, ]

admin.site.register(Stadium, StadiumAdmin)

class MatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(Match, MatchAdmin)


class GuessAdmin(admin.ModelAdmin):
    pass

admin.site.register(Guess, GuessAdmin)


class CulturalProgrammingAdmin(admin.ModelAdmin):
    pass

admin.site.register(CulturalProgramming, CulturalProgrammingAdmin)


class TeamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)


class LocalsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Locals, LocalsAdmin)


class GuessMatchAdmin(admin.ModelAdmin):
    pass

admin.site.register(GuessMatch, GuessMatchAdmin)
