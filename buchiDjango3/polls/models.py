import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# ----------- ----------- ----------- ----------- ----------- 
# Field インスタンスそれぞれの名前(例: question_text や pub_date)は、
# 機械可読なフィールド名です。
# このフィールド名はPythonコードで使うとともに、データベースも列の名前
# として使うことになります。

# https://docs.djangoproject.com/ja/3.0/ref/models/fields/#field-types

# フィールドの型
# AutoField
# BigAutoField
# BigIntegerField
# BinaryField
# BooleanField
# CharField
# DateField
# DateTimeField
# DecimalField
# DurationField
# EmailField
# FileField
# FileField と FieldFile
# FilePathField
# FloatField
# ImageField
# IntegerField
# GenericIPAddressField
# NullBooleanField
# PositiveIntegerField
# PositiveSmallIntegerField
# SlugField
# SmallIntegerField
# TextField
# TimeField
# URLField
# UUIDField
  
# フィールドオプション
# null
# blank
# choices
# db_column
# db_index
# db_tablespace
# default
# editable
# error_messages
# help_text
# primary_key
# unique
# unique_for_date
# unique_for_month
# unique_for_year
# verbose_name
# validators



