import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class LearnGroup(models.Model):
    title = models.CharField(verbose_name="组名", max_length=12)

    def __str__(self):
        return f'title:{self.title}'


class Teacher(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=20)

    def __str__(self):
        return f'teacher_name:{self.name}'


class Student(models.Model):
    id = models.AutoField(primary_key=True)

    gender_choice = (
        (0, "未知"),
        (1, "男"),
        (2, "女")
    )

    name = models.CharField(verbose_name="姓名", max_length=20)
    age = models.IntegerField(verbose_name="年龄")
    gender = models.IntegerField(choices=gender_choice, default=0)

    learn_group = models.ForeignKey(to="LearnGroup", on_delete=True)

    teachers = models.ManyToManyField(to="Teacher")

    def __str__(self):
        return f'student:{self.name}'

    class Meta:
        verbose_name = "学生"
        verbose_name_plural = "学生管理"
