from django.db import models
from account.models import User, UserSerializer
from rest_framework import serializers


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
