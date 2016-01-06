from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() #new instance of firefox
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit() # after every, shut down

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def enter_a_new_item(self, todo_text):
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(todo_text)
        inputbox.send_keys(Keys.ENTER)

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get(self.live_server_url)
        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text #find h1 tag on page, assuming it header we want
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        #She is invited to enter a to-do item straight away
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a To-Do item'
        )
        # She types "Buy peacock feathers" into a textbox
        #her hobby is trying fly-fishing lures
        self.enter_a_new_item('Buy peacock feathers')

        self.check_for_row_in_list_table('1. Buy peacock feathers')

        self.enter_a_new_item('Use peacock feathers to make a fly')

        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table('2. Use peacock feathers to make a fly')

        self.fail('Finish the app!') #until we remove this line, it'll be a failure
