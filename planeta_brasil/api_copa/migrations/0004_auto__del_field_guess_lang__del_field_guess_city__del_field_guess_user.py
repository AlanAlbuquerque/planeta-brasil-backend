# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Guess.lang'
        db.delete_column(u'api_copa_guess', 'lang')

        # Deleting field 'Guess.city'
        db.delete_column(u'api_copa_guess', 'city')

        # Deleting field 'Guess.user_id'
        db.delete_column(u'api_copa_guess', 'user_id')

        # Deleting field 'Guess.country'
        db.delete_column(u'api_copa_guess', 'country')

        # Adding field 'Guess.email'
        db.add_column(u'api_copa_guess', 'email',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Guess.team'
        db.add_column(u'api_copa_guess', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_guess', null=True, to=orm['api_copa.Team']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Guess.lang'
        db.add_column(u'api_copa_guess', 'lang',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Guess.city'
        db.add_column(u'api_copa_guess', 'city',
                      self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Guess.user_id'
        db.add_column(u'api_copa_guess', 'user_id',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Guess.country'
        raise RuntimeError("Cannot reverse this migration. 'Guess.country' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Guess.country'
        db.add_column(u'api_copa_guess', 'country',
                      self.gf('django.db.models.fields.PositiveIntegerField')(),
                      keep_default=False)

        # Deleting field 'Guess.email'
        db.delete_column(u'api_copa_guess', 'email')

        # Deleting field 'Guess.team'
        db.delete_column(u'api_copa_guess', 'team_id')


    models = {
        u'api_copa.culturalprogramming': {
            'Meta': {'object_name': 'CulturalProgramming'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_es': ('django.db.models.fields.TextField', [], {}),
            'description_pt': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_en': ('django.db.models.fields.TextField', [], {}),
            'name_es': ('django.db.models.fields.TextField', [], {}),
            'name_pt': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cultural_programming_photos'", 'null': 'True', 'to': u"orm['api_copa.Photo']"})
        },
        u'api_copa.device': {
            'Meta': {'object_name': 'Device'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '2'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'push_key': ('django.db.models.fields.TextField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'})
        },
        u'api_copa.guess': {
            'Meta': {'object_name': 'Guess'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_guess'", 'null': 'True', 'to': u"orm['api_copa.Team']"})
        },
        u'api_copa.guessmatch': {
            'Meta': {'object_name': 'GuessMatch'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '80'}),
            'hit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matches_guess'", 'null': 'True', 'to': u"orm['api_copa.Match']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'result_home': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'result_visited': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'api_copa.locals': {
            'Meta': {'object_name': 'Locals'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_es': ('django.db.models.fields.TextField', [], {}),
            'description_pt': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_en': ('django.db.models.fields.TextField', [], {}),
            'name_es': ('django.db.models.fields.TextField', [], {}),
            'name_pt': ('django.db.models.fields.TextField', [], {})
        },
        u'api_copa.match': {
            'Meta': {'object_name': 'Match'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'day_match': ('django.db.models.fields.DateTimeField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'result_home': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'result_visited': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'stadium': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matches_stadium'", 'null': 'True', 'to': u"orm['api_copa.Stadium']"}),
            'team_home': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_home'", 'null': 'True', 'to': u"orm['api_copa.Team']"}),
            'team_visited': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams_visited'", 'null': 'True', 'to': u"orm['api_copa.Team']"}),
            'type_match': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'max_length': '1'})
        },
        u'api_copa.news': {
            'Meta': {'object_name': 'News'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_es': ('django.db.models.fields.TextField', [], {}),
            'description_pt': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_en': ('django.db.models.fields.TextField', [], {}),
            'name_es': ('django.db.models.fields.TextField', [], {}),
            'name_pt': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'news_photos'", 'null': 'True', 'to': u"orm['api_copa.Photo']"})
        },
        u'api_copa.photo': {
            'Meta': {'object_name': 'Photo'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'api_copa.stadium': {
            'Meta': {'object_name': 'Stadium'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'api_copa.team': {
            'Meta': {'object_name': 'Team'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_es': ('django.db.models.fields.TextField', [], {}),
            'description_pt': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_app': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_en': ('django.db.models.fields.TextField', [], {}),
            'name_es': ('django.db.models.fields.TextField', [], {}),
            'name_pt': ('django.db.models.fields.TextField', [], {})
        },
        u'api_copa.userphoto': {
            'Meta': {'object_name': 'UserPhoto'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'user_id': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'api_copa.weare': {
            'Meta': {'object_name': 'WeAre'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_es': ('django.db.models.fields.TextField', [], {}),
            'description_pt': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name_en': ('django.db.models.fields.TextField', [], {}),
            'name_es': ('django.db.models.fields.TextField', [], {}),
            'name_pt': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['api_copa']