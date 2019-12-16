# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.db import models


class CommonInfo(models.Model):
    create_datetime = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    update_datetime = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        abstract = True


class AppUser(CommonInfo):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'app_user'
        indexes = [
            models.Index(fields=['user_name', 'create_datetime'], name='idx_user_name_create_datetime')
        ]
        # constraints = [models.UniqueConstraint(fields=['birthday', 'user_name'], name='uq_birthday_username')]
        unique_together = ['user_name', 'birthday']


class AppCars(CommonInfo):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('AppUser', models.DO_NOTHING, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'app_cars'
        index_together = ('user', "product_id")


"""
CREATE TABLE `app_cars` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL COMMENT '客户ID',
  `product_id` int(11) DEFAULT NULL COMMENT '商品id',
  `quantity` int(11) DEFAULT NULL COMMENT '数量',
  `price` int(11) DEFAULT NULL COMMENT '单价',
  `create_datetime` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_datetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `u_c_id` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4


CREATE TABLE `app_user` (
  `id` int(11) NOT NULL,
  `user_name` varchar(255) DEFAULT NULL COMMENT '客户名',
  `birthday` datetime DEFAULT NULL COMMENT '出生日期',
  `create_datetime` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_datetime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

"""
