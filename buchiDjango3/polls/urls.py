from django.urls import path
from . import views

urlpatterns = [

    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

#path(
#    route  必須) ・URL パターンを含む文字列です。パターンはGETやPOSTのパラメーター、そしてドメイン名を検索しません。
#    view   必須) ・Django がマッチする正規表現を見つけると、Django は指定されたビュー関数を呼び出します。
#                 　第一引数にHttpRequest オブジェクトを、
#                 　キーワード引数としてrouteから「キャプチャされた」値を呼び出します。
#    kwargs       ・任意のキーワード引数を辞書として対象のビューに渡せます。
#    name         ・URL に名前付けをしておけば Django のどこからでも明確に参照でき、とくにテンプレートの中で有効です。
#                   この便利な機能のおかげで、プロジェクトのURLにグローバルな変更を加える場合にも1つのファイルを
#                   変更するだけで済むようになります。
#    ),
