from django.test import TestCase, Client
from django.urls import reverse
from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(title='Test Post', story='This is a test post.', location='istanbul', date_format='1', date='2023-05-20T18:20')

    def test_post_detail_view(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.story)

    def test_create_post_view(self):
        url = reverse('create-post')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post')


