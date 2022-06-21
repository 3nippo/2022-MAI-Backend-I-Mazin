from django.db import models
from account.models import User

# Create your models here.
class History(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=False)
    item = models.ForeignKey('SearchItem', models.DO_NOTHING, blank=False)

    results_clicks_num = models.IntegerField(blank=False)
    marketing_clicks_num = models.IntegerField(blank=False)
    pages_viewed_num = models.IntegerField(blank=False)

    class Meta:
        db_table = 'history'


class SearchItem(models.Model):
    question = models.TextField()
    results_num = models.IntegerField()

    class Meta:
        db_table = 'search_items'
