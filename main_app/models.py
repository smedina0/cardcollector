from django.db import models
# import reverse at top
from django.urls import reverse


# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=100)
    game = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card_detail', kwargs={'card_id': self.id})
