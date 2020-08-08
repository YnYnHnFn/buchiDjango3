"""
buchiDjango3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

## Uncomment next two lines to enable admin:
##from django.contrib import admin
##from django.urls import path

#urlpatterns = [
#    # Uncomment the next line to enable the admin:
#    #path('admin/', admin.site.urls)
#]

from django.contrib import admin
from django.urls import include, path

# include() 関数は他の URLconf への参照することができます。 
# Django が include() に遭遇すると、そのポイントまでに一致した
# URL の部分を切り落とし、次の処理のために残りの文字列を
# インクルードされた URLconf へ渡します。
# include() の背景にある考えは、 URL を簡単にプラグ & プレイ可能にする
# ことです。polls には独自の URLconf (polls/urls.py) を持っているので、
# "/polls/" 、 "/fun_polls/" や、 "/content/polls/" といった、
# どんなパスルート下にも置けて、どこに置いてもきちんと動作します。

urlpatterns = [

    path('polls/', include('polls.urls')),
    # polls下のurls.py に行くように！

    # URLパターンをインクルードするときはいつでも include() を使うべきです。 
    # admin.site.urls はこれについての唯一の例外です。
    path('admin/', admin.site.urls),

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
