from tortoise.models import Model
from tortoise import Tortoise, fields


class Persone(Model):
    name = fields.CharField(200)
    email = fields.CharField(200)
    phone = fields.CharField(200)
    password = fields.CharField(200)


Tortoise.init_models(['user.models'], 'models')



