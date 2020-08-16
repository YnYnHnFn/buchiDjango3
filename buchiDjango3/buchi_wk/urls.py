from django.urls import path
from . import views

#Django にどのアプリのものが判断可能にさせるために名前空間を明らかにする。
app_name = 'buchi_wk'


#path(
#    route  必須) ・URL パターンを含む文字列です。パターンはGETやPOSTのパラメーター、そしてドメイン名を検索しません。
#    view   必須) ・Django がマッチする正規表現を見つけると、Django は指定されたビュー関数を呼び出します。
#                 　第一引数にHttpRequest オブジェクトを、
#                 　キーワード引数としてrouteから「キャプチャされた」値を呼び出します。
#    kwargs       ・任意のキーワード引数を辞書として対象のビューに渡せます。
#    name         ・URL に名前付けをしておけば Django のどこからでも明確に参照でき、とくにテンプレートの中で有効です。
#                   テンプレートで私を書くときはこの名前を使ってくれ。

urlpatterns = [

    path('', views.index, name='index'),

    #path('try_', views.index, name='try_hoge'),

    path('try_bootstrap.html', views.try_bootstrap, name='try_bootstrap'),
    path('try_font.html', views.try_font, name='try_font'),
    path('try_fontawesome.html', views.try_fontawesome, name='try_fontawesome'),



]
