from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _


class Warehouse(models.Model):
    name = models.CharField(_('Name'), max_length=256)


class Unit(models.Model):
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, related_name='units')
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='units')


class Shelf(models.Model):
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, related_name='shelves')


class Box(models.Model):
    shelf = models.ForeignKey('Shelf', on_delete=models.CASCADE, related_name='boxes')


class Item(models.Model):
    name = models.CharField(_('Name'), max_length=256)
    box = models.ForeignKey('Box', on_delete=models.CASCADE, related_name='items')


class Organization(models.Model):
    name = models.CharField(_('Name'), max_length=256)


class User(AbstractUser):
    pass


class Membership(models.Model):
    UNIT_ADMIN = 'unit_admin'
    SHELF_ADMIN = 'shelf_admin'
    BASIC_USER = 'basic_user'
    ROLES = (
        (UNIT_ADMIN, _('Unit Admin')),
        (SHELF_ADMIN, _('Shelf Admin')),
        (BASIC_USER, _('Basic User')),
    )
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='memberships')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='memberships')
    role = models.CharField(_('Role'), choices=ROLES, max_length=32)
