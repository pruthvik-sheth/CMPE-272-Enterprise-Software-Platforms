import unittest
from unittest.mock import patch
from app import app

# Written by Jayanth Kalyanam and Meghkumar Patel

class TestMastodonAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # Mock testing create post API
    @patch('app.mastodon.status_post')
    def test_create_post(self, mock_status_post):
        mock_status_post.return_value = {'id': str(1), 'content': 'Test post'}
        response = self.app.post('/post', json={'content': 'Test post'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'id': str(1), 'content': 'Test post'})

    # Mock testing retrieve post API
    @patch('app.mastodon.status')
    def test_get_post(self, mock_status):
        mock_status.return_value = {'id': str(1), 'content': 'Test post'}
        response = self.app.get('/retrieve/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'id': str(1), 'content': 'Test post'})

    # Mock testing delete post API
    @patch('app.mastodon.status_delete')
    def test_delete_post(self, mock_status_delete):
        mock_status_delete.return_value = None
        response = self.app.delete('/delete/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()