from django.db import models

"""
    <input type="radio" name="applicationSystem" value="1" checked>
    <label>备考题源集</label>
    <input type="radio" name="applicationSystem" value="2">
    <label>冲刺模拟题</label>
    <input type="radio" name="applicationSystem" value="3">
    <label>最后的冲刺</label>
"""


# Create your models here.
class ItemsInfo(models.Model):
    ItemNo = models.IntegerField()
    CorrectAnswer = models.CharField(max_length=2)
    ItemDesc = models.CharField(max_length=3000)

