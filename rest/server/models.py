from django.db import models


# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=100, verbose_name="产品名称")
    p_price = models.IntegerField(verbose_name="价格")
    p_unit = models.CharField(verbose_name="单位", max_length=10)

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品管理"
        db_table = "server_product"
        # index_together = ['p_name']
