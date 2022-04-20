import unittest
from webapp import create_app


class TestControllers(unittest.TestCase):
    def setUp(self):
        app = create_app('config.TestConfig')
        self.client = app.test_client()

    def test_ping(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.text, 'Hello from Manggo!')


if __name__ == '__main__':
    unittest.main()
