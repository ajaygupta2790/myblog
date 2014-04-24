# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'Comment'
        db.create_table(u'blog_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'blog', ['Comment'])

        # Adding model 'Travel'
        db.create_table(u'blog_travel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'blog', ['Travel'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'Comment'
        db.delete_table(u'blog_comment')

        # Deleting model 'Travel'
        db.delete_table(u'blog_travel')


    models = {
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"})
        },
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'blog.travel': {
            'Datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Travel'},
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['blog']