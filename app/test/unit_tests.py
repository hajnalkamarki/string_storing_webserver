import unittest

from flask import json
from app import app


class AppendTester(unittest.TestCase):
    """
    This class is for testing the /append endpoint.
    """

    def setUp(self):
        self.app = app.test_client()

    def test_append_data(self):
        """
        Test for appending data correctly.

        :return:
        """
        data = json.dumps({
            'item': 'test_item'
        })
        response = self.app.put('append',
                                headers={'Content-Type': 'application/json'},
                                data=data)
        self.assertEqual(200, response.status_code)

    def test_send_wrong_data(self):
        """
        Test for trying to append incorrect data.

        :return:
        """
        data = json.dumps({
            'not_item': 'test_item'
        })
        response = self.app.put('append',
                                headers={'Content-Type': 'application/json'},
                                data=data)
        self.assertEqual(400, response.status_code)

    def test_send_empty_request(self):
        """
        Test for trying to append None.

        :return:
        """
        data = json.dumps({})
        response = self.app.put('append',
                                headers={'Content-Type': 'application/json'},
                                data=data)
        self.assertEqual(400, response.status_code)


class ShowTester(unittest.TestCase):
    """
    This class is for testing the /show endpoint.
    """

    def setUp(self):
        self.app = app.test_client()

    def test_show_data(self):
        """
        Test for getting data back.

        :return:
        """
        response = self.app.get('show',
                                headers={'Content-Type': 'application/json'})
        self.assertEqual(200, response.status_code)

    def test_show_data_with_data(self):
        """
        Test for getting data back when the request is not empty, it should make no difference.

        :return:
        """
        data = json.dumps({
            'item': 'test_item'
        })
        response = self.app.get('show',
                                headers={'Content-Type': 'application/json'},
                                data=data)
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
