# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bet.stubborns'
        db.add_column(u'megasena_bet', 'stubborns',
                      self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Bet.stubborns'
        db.delete_column(u'megasena_bet', 'stubborns')


    models = {
        u'megasena.bet': {
            'Meta': {'ordering': "['concourse', '-hits']", 'object_name': 'Bet'},
            'concourse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['megasena.Concourse']"}),
            'hits': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n01': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'n02': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'n03': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'n04': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'n05': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'n06': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'stubborns': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'})
        },
        u'megasena.concourse': {
            'Meta': {'ordering': "['-concourse']", 'object_name': 'Concourse'},
            'concourse': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'megasena.files': {
            'Meta': {'object_name': 'Files'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'megasena.raffle': {
            'Meta': {'ordering': "['-raffle_date']", 'object_name': 'Raffle'},
            'accumulated_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'accumulated_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'collected_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'concourse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['megasena.Concourse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n01': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'n02': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'n03': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'n04': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'n05': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'n06': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'prize_next': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'prize_turnaround': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'quadra_share': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'quadra_winners': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'quina_share': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'quina_winners': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'raffle_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sena_share': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sena_winners': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['megasena']