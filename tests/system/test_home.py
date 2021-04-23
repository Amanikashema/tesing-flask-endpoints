from unittest import TestCase
from tests import main
import json


class TestHome(TestCase):
    def test_home(self):
        with main.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {'message': 'hello, world!'})



