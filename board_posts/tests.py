from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTableTest(TestCase):

    def setUp(self):
        Post.objects.create(text='This is only for test')

    
    def test_post_content(self):
        post = Post.objects.get(pk=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'This is only for test')

class IndexPageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="second test")
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/') #http://localhost:8000/
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_by_name(self):
        # build path 
        #http://localhost:8000/
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index')) #http://localhost:8000/
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')  