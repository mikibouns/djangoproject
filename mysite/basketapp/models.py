from django.db import models
from django.conf import settings
from mainapp.models import CollectionsImg

class Basket(models.Model):
    basket_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='user')
    basket_product = models.ForeignKey(CollectionsImg, on_delete=models.CASCADE, verbose_name='product')
    basket_quantity = models.PositiveIntegerField(verbose_name='quantity', default=0)
    basket_datetime = models.DateTimeField(verbose_name='time_of_addition', auto_now_add=True)

    def __str__(self):
        return self.basket_user


