from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table='post'

    name=models.CharField(
        'Name',blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body=models.CharField(
        'body',blank=True, null=True, max_length=120, db_index=True
    )
    created_at = models.DateTimeField(
        'Created Date',blank=True, auto_now_add=True
    )
