from django.db import models
from enum import Enum


class Letters(models.Model):
    name_post = models.TextField()
    name_get = models.TextField()
    loc_post = models.TextField()
    loc_get = models.TextField()
    index_post = models.IntegerField()
    index_get = models.IntegerField()
    type_letter = [
        (1, 'Letter'),
        (2, 'Custom_letter'),
        (3, 'Valuable_letter'),
        (4, 'Express_letter'),
    ]
    weight_letter = models.FloatField()


class Parcels(models.Model):
    name_post = models.TextField()
    name_get = models.TextField()
    loc_post = models.TextField()
    loc_get = models.TextField()
    index_post = models.IntegerField()
    index_get = models.IntegerField()
    phone = models.IntegerField()
    type_parcel = [
        (1, 'Small'),
        (2, 'Parcel'),
        (3, 'Parcel_first_class'),
        (4, 'Valuable_parcel'),
        (5, 'International_parcel'),
        (6, 'Express_parcel'),

    ]
    # type_parcel = models.IntegerField()
    weight_letter = models.FloatField()

    # class TypeParcel(Enum):
    #     SMALL = 1
    #     CUSTOM_LETTER = 2
    #     VALUABLE_LETTER = 3
    #     EXPRESS_LETTER = 4
