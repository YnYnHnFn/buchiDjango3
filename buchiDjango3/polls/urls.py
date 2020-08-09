from django.urls import path
from . import views

#Django にどのアプリのものが判断可能にさせるために名前空間を明らかにする。
app_name = 'polls'


#path(
#    route  必須) ・URL パターンを含む文字列です。パターンはGETやPOSTのパラメーター、そしてドメイン名を検索しません。
#    view   必須) ・Django がマッチする正規表現を見つけると、Django は指定されたビュー関数を呼び出します。
#                 　第一引数にHttpRequest オブジェクトを、
#                 　キーワード引数としてrouteから「キャプチャされた」値を呼び出します。
#    kwargs       ・任意のキーワード引数を辞書として対象のビューに渡せます。
#    name         ・URL に名前付けをしておけば Django のどこからでも明確に参照でき、とくにテンプレートの中で有効です。
#                   テンプレートで私を書くときはこの名前を使ってくれ。

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #<question_id> から <pk> に変更

    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #<question_id> から <pk> に変更

    path('<int:question_id>/vote/', views.vote, name='vote'),

    # 汎用ビューを使う前
    #path('', views.index, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]

# --------- --------- --------- --------- --------- --------- --------- --------- 
# ↑↑↑↑↑汎用ビューを使う: コードが少ないのはいいことだ
#           Django では、汎用ビュー（generic view）というショートカットを提供しています。
# --------- --------- --------- --------- --------- --------- --------- --------- 

#urlpatterns = [
#
#    #上位の urls.pyにて こう「path('polls/', include('polls.urls')),」書いてあり、
#    #ここでは その後ろからディスパッチ
#
#    # ex: /polls/
#    path('', views.index, name='index'),
#
#    # ex: /polls/5/
#    path('<int:question_id>/', views.detail, name='detail'),
#    # 結果、↓こんな風に呼び出される。
#    # detail(request=<HttpRequest object>, question_id=34) ※question_id=34がポイントだね。
#
#    # ex: /polls/5/results/
#    path('<int:question_id>/results/', views.results, name='results'),
#
#    # ex: /polls/5/vote/
#    path('<int:question_id>/vote/', views.vote, name='vote'),
#]

