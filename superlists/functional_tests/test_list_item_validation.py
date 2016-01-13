from unittest import skip
from .base import TodoFunctionalTest

class ItemValidationTest(TodoFunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        #She hits "enter" on the empty item box
        self.enter_a_new_item('')

        #The home page refreshes and there is an error messages
        #saying that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some etext for the item
        # which now works
        self.enter_a_new_item('Buy milk')
        self.check_for_row_in_list_table('1. Buy milk')

        # Edith perversely tries to enter a second blank item
        self.enter_a_new_item('')
        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # and she can correct it by filling some text in.
        self.enter_a_new_item('Make tea')
        self.check_for_row_in_list_table('Buy milk')
        self.check_for_row_in_list_table('Make tea')
