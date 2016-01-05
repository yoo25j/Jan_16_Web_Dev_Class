from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() #new instance of firefox
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit() # after every, shut down

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard abot a call new online to-do app
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text #find h1 tag on page, assuming it header we want
        self.assertIn('To-Do', header_text)

        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_ new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter to-do item'
        )
        # She types "Buy peacock feathers" into a textbox
        #her hobby is trying fly-fishing lures
        inputbox.send_keys('Buy peacock featers')
        #When she hits enter, the page updates, and now the page lists
        #1. Buy peacock feathers as the item in a to-do lists
        inputbox.send_keys(Keys.ENTER) # Keys is new thing we havne't referrred to yet, import it

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_Tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Buy peacock featers' for row in rows) #useful in that its quick and dirty #right now it is becoming a bad decision, gets us further
        )
        #There is still a textbox inviting her to add another item
        # She enters 'Use peacock feathers to make fly'
        # She is very methdolical

        # The homepage updates again, and now shows both items on her lists

        #Edith wonders whether the site will remember her list. Then she sees
        #that the site has generated a unique URL for her -- there is some
        #explanatory text to that effect.

        #She visits that URL - her to-do list is still there

        #satisfied, she goes back to sleep
        #browser.quit()
        self.fail('Finish the app!') #until we remove this line, it'll be a failure

if __name__ == '__main__':
    unittest.main() #main method, ignore warning
