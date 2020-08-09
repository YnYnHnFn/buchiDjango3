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

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# --------- --------- --------- --------- 
# #def index(request):
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

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    # 公開日降順で５件取得
#
#    context = {
#        'latest_question_list': latest_question_list
#    }
#    return render(request, 'polls/index.html', context)
#    # render() 関数は、
#    # 第1引数として request オブジェクトを、
#    # 第2引数としてテンプレート名を、
#    # 第3引数（任意）として辞書を受け取ります。
#    # この関数はテンプレートを指定のコンテキストでレンダリングし、
#    # その HttpResponse オブジェクトを返します。

## ↓ 汎用ビューを使う:（generic view）というショートカットがあります
##    def から class に変わってます。

class IndexView(generic.ListView):  #一覧系は generic.ListView を継承

    #デフォルトでは一覧系は <app name>/<model name>_list.html がテンプレート名
    #変更したい場合だけ template_name を指定。
    template_name = 'polls/index.html'

    #汎用ビューではコンテキスト変数は モデル名より自動的に生成されます。小文字。
    #DetailView なら <model name>、ListView なら <model name>_list
    #これを使わない場合は context_object_name 属性で指定。
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


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
##                    これは get() ではなく、 filter() を使い、リストが空の場合 Http404 を送出します。

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {'question': question})

## ↓ 汎用ビューを使う:（generic view）というショートカットがあります

class DetailView(generic.DetailView):

    model = Question

    #デフォルトでは単票系は <app name>/<model name>_detail.html がテンプレート名
    #変更したい場合だけ template_name を指定。
    template_name = 'polls/detail.html'

    #汎用ビューではコンテキスト変数は モデル名より自動的に生成されます。小文字。
    #DetailView なら <model name>、ListView なら <model name>_list

# --------- --------- --------- --------- 
#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

## ↓ 結果のテンプレート使う

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/results.html', {'question': question})

## ↓ 汎用ビューを使う:（generic view）というショートカットがあります

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# --------- --------- --------- --------- 
#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)

## ↓ form化

def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        #request.POST は辞書のようなオブジェクトです。request.POST の値は常に文字列です。
        #キー（'choice'）を指定すると、送信したデータにアクセスできます。
        #この場合、 選択された選択肢の ID を文字列として返します。 
        #request.GETもあるよ。

    except (KeyError, Choice.DoesNotExist):
    
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else: #try 正常時の分岐ね。

        selected_choice.votes += 1        ###これ、競合考慮されてないんだけどね。。
        selected_choice.save()
        # POSTデータを正常に処理した後は、常にHttpResponseRedirectを返します。
        # これにより、ユーザーが[戻る]ボタンを押した場合にデータが2回投稿されるのを防ぎます。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

        #この例では、 HttpResponseRedirect コンストラクタの中で reverse() 関数を使用しています。
        #この関数を使うと、ビュー関数中での URL のハードコードを防げます。関数には、
        #制御を渡したいビューの名前と、そのビューに与える URL パターンの位置引数を与えます。
        #reverse() を呼ぶと、文字列が返ってきます。'/polls/3/results/' ※この 3 は question.id の値

