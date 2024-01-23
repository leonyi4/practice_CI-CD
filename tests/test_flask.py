import unittest
from source.app import app

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')

    def test_404_not_found(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

    def test_post_method_not_allowed(self):
        response = self.app.post('/')
        self.assertEqual(response.status_code, 405)

    def test_invalid_route_returns_404(self):
        response = self.app.get('/invalid-route')
        self.assertEqual(response.status_code, 404)

    def test_response_content_type_json(self):
        response = self.app.get('/')
        self.assertIn('text/html', response.content_type)

if __name__ == '__main__':
    unittest.main()
