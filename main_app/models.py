from django.db import models
# import reverse at top
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vendor_detail", kwargs={"vendor_id": self.id})


class Card(models.Model):
    name = models.CharField(max_length=100)
    game = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    vendors = models.ManyToManyField(Vendor)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card_detail', kwargs={'card_id': self.id})


class Cleaning(models.Model):
    TOOLS = (
        ('C', 'Cotton Swab'),
        ('B', 'Brush'),
        ('S', 'Sponge'),
        ('P', 'Paper Towel'),
        ('A', 'Air Duster'),
        ('O', 'Other')
    )

    date = models.DateField('cleaning date')
    tool = models.CharField(max_length=1, choices=TOOLS,
                            default=TOOLS[0][0], verbose_name='cleaning tool')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tool_display()} on {self.date}"

    class Meta:
        ordering = '-date',
