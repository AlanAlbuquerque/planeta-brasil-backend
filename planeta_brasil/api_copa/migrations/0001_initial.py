# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guess'
        db.create_table(u'api_copa_guess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('country', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('user_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('lang', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'api_copa', ['Guess'])

        # Adding model 'Device'
        db.create_table(u'api_copa_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('os', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('push_key', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.CharField')(default='1', max_length=2)),
        ))
        db.send_create_signal(u'api_copa', ['Device'])

        # Adding model 'News'
        db.create_table(u'api_copa_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name_pt', self.gf('django.db.models.fields.TextField')()),
            ('name_en', self.gf('django.db.models.fields.TextField')()),
            ('name_es', self.gf('django.db.models.fields.TextField')()),
            ('description_pt', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_es', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='news_photos', null=True, to=orm['api_copa.Photo'])),
        ))
        db.send_create_signal(u'api_copa', ['News'])

        # Adding model 'Photo'
        db.create_table(u'api_copa_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'api_copa', ['Photo'])

        # Adding model 'UserPhoto'
        db.create_table(u'api_copa_userphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('user_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('lang', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
        ))
        db.send_create_signal(u'api_copa', ['UserPhoto'])

        # Adding model 'Team'
        db.create_table(u'api_copa_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name_pt', self.gf('django.db.models.fields.TextField')()),
            ('name_en', self.gf('django.db.models.fields.TextField')()),
            ('name_es', self.gf('django.db.models.fields.TextField')()),
            ('description_pt', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_es', self.gf('django.db.models.fields.TextField')()),
            ('img_app', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'api_copa', ['Team'])

        # Adding model 'Stadium'
        db.create_table(u'api_copa_stadium', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'api_copa', ['Stadium'])

        # Adding model 'Match'
        db.create_table(u'api_copa_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('team_home', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_home', null=True, to=orm['api_copa.Team'])),
            ('team_visited', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='teams_visited', null=True, to=orm['api_copa.Team'])),
            ('stadium', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='matches_stadium', null=True, to=orm['api_copa.Stadium'])),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('type_match', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1, max_length=1)),
            ('result_home', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('result_visited', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('day_match', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_finished', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'api_copa', ['Match'])

        # Adding model 'Locals'
        db.create_table(u'api_copa_locals', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name_pt', self.gf('django.db.models.fields.TextField')()),
            ('name_en', self.gf('django.db.models.fields.TextField')()),
            ('name_es', self.gf('django.db.models.fields.TextField')()),
            ('description_pt', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')()),
            ('description_es', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'api_copa', ['Locals'])

        # Adding model 'GuessMatch'
        db.create_table(u'api_copa_guessmatch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=80)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='matches_guess', null=True, to=orm['api_copa.Match'])),
            ('result_home', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('result_visited', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('hit', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'api_copa', ['GuessMatch'])


    def backwards(self, orm):
        # Deleting model 'Guess'
        db.delete_table(u'api_copa_guess')

        # Deleting model 'Device'
        db.delete_table(u'api_copa_device')

        # Deleting model 'News'
        db.delete_table(u'api_copa_news')

        # Deleting model 'Photo'
        db.delete_table(u'api_copa_photo')

        # Deleting model 'UserPhoto'
        db.delete_table(u'api_copa_userphoto')

        # Deleting model 'Team'
        db.delete_table(u'api_copa_team')

        # Deleting model 'Stadium'
        db.delete_table(u'api_copa_stadium')

        # Deleting model 'Match'
        db.delete_table(u'api_copa_match')

        # Deleting model 'Locals'
        db.delete_table(u'api_copa_locals')

        # Deleting model 'GuessMatch'
        db.delete_table(u'api_copa_guessmatch')


    models = {
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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'user_id': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
        }
    }

    complete_apps = ['api_copa']