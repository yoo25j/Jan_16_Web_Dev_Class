from django.core.urlresolvers import resolve
from django.utils.html import escape
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from lists.models import Item, List
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

class NewListTest(TestCase):
    def test_home_can_save_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data = {'item_text' : 'A new list item'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data = {'item_text' : 'A new list item'}
        )
        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/' % (new_list.id,))

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("You can't have an empty list item")
        #print(response.content.decode())
        self.assertContains(response, expected_error)

    def test_invalid_list_items_arent_saved(self):
        self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        new_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (new_list.id,))
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_list(self):
        new_list = List.objects.create()
        Item.objects.create(text= 'itemey 1', list = new_list)
        Item.objects.create(text='itemey 2', list = new_list)

        other_list = List.objects.create()
        Item.objects.create(text= 'other item 1', list = other_list)
        Item.objects.create(text='other item 2', list = other_list)

        response = self.client.get('/lists/%d/' % (new_list.id,))

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')

    def test_passes_correct_list_to_templates(self):
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)

    def test_can_save_a_post_request_to_an_existing_list(self):
        correct_list = List.objects.create()
        self.client.post(
            '/lists/%d/add_item' % (correct_list.id),
            data = {'item_text': 'A new item for an existing list'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_validation_errors_stay_on_list_page(self):
        pass

    def test_invalid_list_items_arent_saved(self):
        pass

    def test_list_view_displays_checkbox(self):
        current_list = List.objects.create()
        Item.objects.create(text="Item 1", list = current_list)
        Item.objects.create(text="Item 2", list = current_list)

        response = self.client.get('/lists/%d/' % (current_list.id))

        self.assertContains(response, 'input type = "checkbox"')

    def test_POST_item_toggles_done(self):
        current_list = List.objects.create()
        item1 = Item.objects.create(text="Item 1", list = current_list)
        item2 = Item.objects.create(text="Item 2", list = current_list)

        #POST data
        response = self.client.post(
            '/lists/%d/items/' % (current_list.id),
            data={'mark_item_done' : item1.id}
        )
        self.assertRedirects(response, '/lists/%d/' % (current_list.id))

        item1 = Item.objects.get(id = item1.id)
        item2 = Item.objects.get(id = item2.id)

        self.assertTrue(item1.is_done)
        self.assertFalse(item2.is_done)
