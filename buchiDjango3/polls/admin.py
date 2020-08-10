from django.contrib import admin

from .models import Choice, Question

# Register your models here.
# ここに登録することで、既定の管理画面上にDBメンテの対象として出てくる。

### --------- class宣言 ---------

#class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3   #新規追加エリア、３つ用意。

## ↓↓ 表形式に(StackedInline→TabularInline)

class ChoiceInline(admin.TabularInline ):
    model = Choice
    extra = 3   #新規追加エリア、３つ用意。

### --------- 

#class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

## ↓↓フィールドセット使う。

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 外部結合テーブルを一緒に出しちゃう。
    inlines = [ChoiceInline]

    # 「変更する question を選択」画面で。
    #
    # 各項目表示：カラム表示したいフィールドの名前をタプルにして指定します。
    # メソッドの戻り値も項目に並べられます。
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # フィルタ (Filter)：サイドバーができ、チェンジリストを pub_date 
    # フィルタの種類は、フィルタ対象のフィールドの種類に応じて変化します。
    list_filter = ['pub_date']
    # 日付型の階層型フィルタ
    date_hierarchy = 'pub_date'
    # 検索機能。舞台裏では LIKE クエリを使う
    search_fields = ['question_text']
    # 1ページ10行。デフォルトは100。
    list_per_page = 10


### --------- ↓site.register デコレータ --------- 

# admin.site.register(Question)     # とりあえずは こう書いとけばOK♪

## ↓↓ モデルの admin のオプションを変更（並びとか、グループ見出し）したいときには、
## 　　 モデルごとに admin クラスを作成（QuestionAdmin）して、
##      admin.site.register()の2番目の引数に渡す。

admin.site.register(Question, QuestionAdmin)

# 外部結合テーブル個別配置
admin.site.register(Choice)

