from django.contrib import admin

# Register your models here.

# ここに登録することで、既定の管理画面上にDBメンテの対象として出てくる。

from .models import Question

admin.site.register(Question)
