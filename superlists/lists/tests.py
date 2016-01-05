from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page


class HomePageTest(TestCase): #extends test case
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') #matches every string past domain name #ex: app.me(**after this domain name)/lisis/123ab
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #represents url request, python abstraction for what a browser what look for that value
        response = home_page(request)
        expected_html = render_to_string('home.html') #after deleting tests below, put in this
        self.assertEqual(response.content.decode(), expected_html)

        # self.assertTrue(response.content.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith('</html>'))


        # class SmokeTest(TestCase):
        #     def test_bad_maths(self): #failing test
        #         self.assertEqual(1+1,3)
