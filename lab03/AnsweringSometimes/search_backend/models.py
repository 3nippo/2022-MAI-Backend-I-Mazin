from django.db import models
from account.models import Users

# Create your models here.
class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    item = models.ForeignKey('SearchItems', models.DO_NOTHING)
    results_clicks_num = models.IntegerField()
    marketing_clicks_num = models.IntegerField()
    pages_viewed_num = models.IntegerField()

    class Meta:
        db_table = 'history'


class SearchItems(models.Model):
    item_id = models.AutoField(primary_key=True)
    question = models.TextField()
    results_num = models.IntegerField()

    class Meta:
        db_table = 'search_items'
