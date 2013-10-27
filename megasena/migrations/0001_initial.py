# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Files'
        db.create_table(u'megasena_files', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'megasena', ['Files'])

        # Adding model 'Concourse'
        db.create_table(u'megasena_concourse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('concourse', self.gf('django.db.models.fields.IntegerField')(unique=True, max_length=4)),
        ))
        db.send_create_signal(u'megasena', ['Concourse'])

        # Adding model 'Raffle'
        db.create_table(u'megasena_raffle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('concourse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megasena.Concourse'])),
            ('raffle_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('n01', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('n02', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('n03', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('n04', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('n05', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('n06', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('collected_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('sena_winners', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('sena_share', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('quina_winners', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('quina_share', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('quadra_winners', self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True, blank=True)),
            ('quadra_share', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('accumulated_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('accumulated_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('prize_next', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('prize_turnaround', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'megasena', ['Raffle'])

        # Adding model 'Bet'
        db.create_table(u'megasena_bet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('concourse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['megasena.Concourse'])),
            ('n01', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('n02', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('n03', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('n04', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('n05', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('n06', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('hits', self.gf('django.db.models.fields.IntegerField')(max_length=1, null=True, blank=True)),
        ))
        db.send_create_signal(u'megasena', ['Bet'])


    def backwards(self, orm):
        # Deleting model 'Files'
        db.delete_table(u'megasena_files')

        # Deleting model 'Concourse'
        db.delete_table(u'megasena_concourse')

        # Deleting model 'Raffle'
        db.delete_table(u'megasena_raffle')

        # Deleting model 'Bet'
        db.delete_table(u'megasena_bet')


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