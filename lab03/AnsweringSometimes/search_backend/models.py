from django.db import models
from account.models import User, UserSerializer
from rest_framework import serializers
import hashlib
from datetime import datetime


class SearchItem(models.Model):
    question = models.TextField()
    results_num = models.IntegerField()

    class Meta:
        db_table = 'search_items'

class SearchItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchItem
        fields = ['question', 'results_num']


class History(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=False)
    item = models.ForeignKey(SearchItem, models.DO_NOTHING, blank=False)

    results_clicks_num = models.IntegerField(blank=False)
    marketing_clicks_num = models.IntegerField(blank=False)
    pages_viewed_num = models.IntegerField(blank=False)

    class Meta:
        db_table = 'history'

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    item = SearchItemSerializer()

    class Meta:
        model = History
        fields = ['user', 'item', 'results_clicks_num', 'marketing_clicks_num', 'pages_viewed_num']


def picture_path(instance, filename):
    secs = int(datetime.now().timestamp())
    salted_bytes = bytearray(filename.encode()) + secs.to_bytes((secs.bit_length() + 7) // 8, 'big')
    return 'user_{0}/{1}'.format(instance.id, hashlib.sha256(salted_bytes).hexdigest())

class PictureSearchItem(models.Model):
    avatar = models.ImageField(upload_to=picture_path, blank=False)
    question = models.TextField()

    class Meta:
        db_table = 'picture_search_items'
