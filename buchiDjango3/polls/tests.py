"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#import django
#from django.test import TestCase
#
## TODO: Configure your database in settings.py and sync before running tests.
#
#class SimpleTest(TestCase):
#    """Tests for the application views."""
#
#    # Django requires an explicit setup() when running tests in PTVS
#    @classmethod
#    def setUpClass(cls):
#        super(SimpleTest, cls).setUpClass()
#        django.setup()
#
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.assertEqual(1 + 1, 2)

## ---------- ---------- ---------- ---------- ---------- ---------- ---------- 
## ↑ 規定でできたもの？
## ↓ tutorialの教え
## ---------- ---------- ---------- ---------- ---------- ---------- ---------- 
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

#(env)>python manage.py test polls
#
#・manage.py test polls は、polls アプリケーション内にあるテストを探します
#・django.test.TestCase クラスのサブクラスを発見します
#・テストのための特別なデータベースを作成します
#・テスト用のメソッドとして、test で始まるメソッドを探します
#・test_was_published_recently_with_future_question を見つけます。その中で、
#　pub_date フィールドに今日から30日後の日付を持つ Question インスタンスが作成されます
#・そして最後に、 assertIs() メソッドを使うことで、本当に返してほしいのは False だったにもかかわらず、
#　was_published_recently() が True を返していることを発見します

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date 
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)



def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    """
    この関数によって、 question 作成処理のコード重複をなくしています。
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        # question を1つも作りませんが、 "No polls are available." 
        # というメッセージが表示されていることをチェックし、
        # latest_question_list が空になっているか確認しています。

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)

        # 追加のアサーションメソッドを提供していることに注意してください。
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        # question を作成し、その question がリストに現れるかどうかを検証しています。
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        # pub_date が未来の日付の質問を作っています。
        # データベースは各テストメソッドごとにリセットされるので、
        # この時にはデータベースには最初の質問は残っていません。
        # そのため、index ページにはquestion は1つもありません。

        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
