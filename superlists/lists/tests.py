from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
#extends test case
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        #matches every string past domain name
        #ex: app.me(**after this domain name)/lisis/123ab
        self.assertEqual(found.func, home_page)


# class SmokeTest(TestCase):
#     def test_bad_maths(self): #failing test
#         self.assertEqual(1+1,3)
