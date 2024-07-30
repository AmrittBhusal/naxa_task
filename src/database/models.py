# from tortoise.models import Model
from tortoise import fields,models

class Student(models.Model):
  id = fields.IntField(pk=True)
  name = fields.CharField(max_length=25, null=False)
  dob = fields.DateField(null=False)