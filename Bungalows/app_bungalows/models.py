from django.db import models

class Bungalow(models.Model):

    class cQualite(models.TextChoices):
        Abime = 'Abîmé'
        Okay  = "Okay"
        Bon = "Bon"
    
    # company = models.ForeignKey(
    #     Company,
    #     on_delete=models.CASCADE,
    # ) 
    murQualite = models.CharField(
        max_length = 128,
        choices=cQualite.choices,
        default=cQualite.Bon 
    )
    name = models.CharField(max_length=54, null=True, blank=True)
    

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return "/product/%s/" % (self.p_name)
