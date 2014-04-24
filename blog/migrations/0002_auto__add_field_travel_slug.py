# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Travel.slug'
        db.add_column(u'blog_travel', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default='default', unique_with=['Datetime'], max_length=50, populate_from='name'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Travel.slug'
        db.delete_column(u'blog_travel', 'slug')


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
            'place': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "['Datetime']", 'max_length': '50', 'populate_from': "'name'"})
        }
    }

    complete_apps = ['blog']