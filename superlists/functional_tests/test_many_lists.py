from .base import TodoFunctionalTest

class ManyListsTest(TodoFunctionalTest):

    def change_list_name(self,list_name):
        inputbox = self.browser.get_element_by_id('id_rename_list')
        inputbox.sendkeys(list_name + '\n')

    def test_can_create_and_view_multiple_lists(self):
      self.browser.get(self.live_server_url)
      self.enter_a_new_item('Buy milk')
      self.enter_a_new_item('Buy cheese')
      self.check_for_row_in_list_table('Buy milk')
      self.check_for_row_in_list_table('Buy cheese')

      #she sees she can change a lit name
      self.change_list_name('Groceries')

      self.browser.get(self.live_server_url)
      self.check_for_row_in_list_table('Groceries')

      #edith creates a new list for her art history hw
      self.browser.enter_a_new_item('Read Camille')
      self.browser.get(self.live_server_url)
      self.check_for_row_in_list_table('Groceries')
      self.check_for_row_in_list_table('Read Camille')

      row = self.find_table_row('Groceries')
      row.find_element_by_tag_name('a').click()
      self.check_for_row_in_list_table('Buy milk')
      self.check_for_row_in_list_table('Buy cheese')
