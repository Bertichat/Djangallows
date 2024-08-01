from django.db import models
from app_bungalows.models import Bungalow

class Fourniture(models.Model):
    name = models.CharField(max_length=54, null=True, blank=True)
    compte_base = models.IntegerField(default=0, null=True, blank=True)
    attendu = models.IntegerField(default=0, null=True, blank=True)
    bungalow = models.ForeignKey(
            Bungalow,
            on_delete=models.CASCADE,
        ) 

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return "/product/%s/" % (self.p_name)
