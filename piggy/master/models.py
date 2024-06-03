from django.db import models
choice_item = (('veg','veg'),('Non-veg','Non-veg'),('egg','egg'))

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    item_desc = models.CharField(max_length=50)
    item_type = models.CharField(choices=choice_item,max_length=50)
    photo = models.ImageField()

    def _str_(self):
        return self.item_name