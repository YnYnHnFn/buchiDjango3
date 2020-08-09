## Create your views here.

# 各ビューには二つの役割があります: 
# 一つはリクエストされたページのコンテンツを含む HttpResponse オブジェクトを返すこと、
# もう一つは Http404 のような例外の送出です。
# それ以外の処理はユーザ次第です。
# 
# ビューはデータベースからレコードを読みだしても、読み出さなくてもかまいません。 
# Django のテンプレートシステム、あるいはサードパーティの Python テンプ レートシステムを
# 使ってもよいですし、使わなくてもかまいません。 
# PDF ファイルを生成しても、 XML を出力しても、 ZIP ファイルをその場で生成してもかまいません。 
# Python ライブラリを使ってやりたいことを何でも実現できます。
# 
# Django にとって必要なのは HttpResponse か、あるいは例外です。
# 
# 簡単に、チュートリアルその 2 で解説した Django のデータベース API を使ってみましょう。
# 試しに index() ビューを作ります。
# これは、システム上にある最新の 5 件の質問項目をカンマで区切り、日付順に表示するビューです:


from django.http import HttpResponse     #全部renderにしちゃえばいらない
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

# --------- --------- --------- --------- 
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

## ↓ テンプレート化

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))
#
#    # テンプレートをロードしてコンテキストに値を入れ、
#    # ※コンテキストは、テンプレート変数名を Python オブジェクトにマッピングする辞書
#    # テンプレートをレンダリングした結果を 
#    # HttpResponse オブジェクトで返す。 →→→このショートカットがrender()

## ↓ ショートカット　render()化

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)
    # render() 関数は、
    # 第1引数として request オブジェクトを、
    # 第2引数としてテンプレート名を、
    # 第3引数（任意）として辞書を受け取ります。
    # この関数はテンプレートを指定のコンテキストでレンダリングし、
    # その HttpResponse オブジェクトを返します。


# --------- --------- --------- --------- 
#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

## ↓404 エラーの送出

#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})
#
#    # get() を実行し、オブジェクトが存在しない場合には 
#    # Http404 を送出することは非常によく使われるイディオムです。

## ↓ ショートカット　get_object_or_404()化
##                    get_list_or_404() という関数もあります。
#                     これは get() ではなく、 filter() を使い、リストが空の場合 Http404 を送出します。

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# --------- --------- --------- --------- 
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# --------- --------- --------- --------- 
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
