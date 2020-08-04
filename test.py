from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        """do this before every test"""
        pass

    def tearDown(self):
        """do this after every test"""


    def test_submit_form(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Flask Boggle</h1>', html)


    def test_check_word(self):
        with app.test_client() as client:
            client.get('/')
            with client.session_transaction() as session:
                session['board'] = [['A','C','D','E','F'],['A','C','D','E','F'],['E','C','D','E','F'],['A','C','D','E','F'],['A','C','D','E','F']]
            self.assertIn('board', session)
            
            res = client.get('/check-word?word=aa')
            self.assertEqual(res.status_code, 200)


    def test_check_highscore(self):
        with app.test_client() as client:
            client.get('/')
            with client.session_transaction() as session:
                session['highscore'] = 10
            self.assertIn('highscore', session)


    def test_check_numplays(self):
        with app.test_client() as client:
            client.get('/')
            with client.session_transaction() as session:
                session['numplays'] = 30
            self.assertIn('numplays', session)
 

    def test_post_score(self):
        with app.test_client() as client:
            client.get('/')
            res = client.post('/post-score', json={"score": 20})
            # self.assertEquals(res.json, dict(success=True))
            self.assertEqual(res.status_code, 200)

