from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
from datetime import datetime

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = 'Hello World. We are the world.'
        )
        post_002 = Post.objects.create(
            title = '두 번째 포스트입니다.',
            content = 'Hello World. We are the world.'
        )
        
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        
        soup = BeautifulSoup(response.content, 'html.parser')
        navbar = soup.find('nav')
        self.assertEqual(soup.title.text, 'Clean Blog - Start Bootstrap Theme')
        
        navbar_links = navbar.find_all('a')  # navbar 내의 모든 링크를 찾는 코드
        link_texts = [link.text.strip() for link in navbar_links]  # 각 링크의 텍스트를 가져와 리스트로 만듦
        self.assertIn('Start Bootstrap', link_texts)  # 수정된 부분
        self.assertIn('About', link_texts)  # 수정된 부분
        self.assertIn('Contact', link_texts)  # 수정된 부분
        self.assertIn('Blog', link_texts)  # 수정된 부분
        
        footer = soup.footer
        self.assertIn('상속 test용 푸터', footer.text)
        
        if Post.objects.count() == 0:
            self.assertIn('아직 게시물이 없습니다.', soup.body.text)
        else:
            self.assertGreater(len(soup.body.select('.posttitle')), 1)

    def test_post_detail(self):
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = 'Hello World. We are the world.'
        )
        
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        navbar = soup.find('nav')
        self.assertEqual(soup.title.text, 'Clean Blog - Start Bootstrap Theme')
        
        main_area = soup.find('body')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_001.content, main_area.text)
        self.assertIn('2023년 11월 16일', main_area.text)
            
        navbar_links = navbar.find_all('a')  # navbar 내의 모든 링크를 찾는 코드
        link_texts = [link.text.strip() for link in navbar_links]  # 각 링크의 텍스트를 가져와 리스트로 만듦
        self.assertIn('Start Bootstrap', link_texts)  # 수정된 부분
        self.assertIn('About', link_texts)  # 수정된 부분
        self.assertIn('Contact', link_texts)  # 수정된 부분
        self.assertIn('Blog', link_texts)  # 수정된 부분
        
        footer = soup.footer
        self.assertIn('상속 test용 푸터', footer.text)
