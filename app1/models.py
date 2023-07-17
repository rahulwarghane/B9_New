from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default = True)
    # is_active = models.BooleanField(default = True)

    class Meta():
        db_table = "book"


    def __str__(self):
        return self.name