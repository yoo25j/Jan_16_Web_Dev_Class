from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox() #new instance of firefox
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()                # after every, shut down

    def test_can_start_a_list_and_retrieve_it_later(self):

    #def test_can_log_in_to_a_new_account(self):

        # write test first before writing the program
        # Edith has heard abot a call new online to-do app
        # She goes to check out its homepage
        #browser = webdriver.Firefox()
        #start a portal 8000
        #go to the homepage
        self.browser.get('http://localhost:8000')
        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        #assert 'Django' in browser.title #only takes in boolean parameters

        #the last line is similar to the following:
        #if ! 'django' in browser.title:
        #   throw new AssertionError


        #functional test, acceptance test, End to End (meaning from the point view of user)


        #She is invited to enter a to-do item straight away
        # She types "Buy peacock feathers" into a textbox
        #her hobby is trying fly-fishing lures

        #When she hits enter, the page updates, and now the page lists
        #1. Buy peacock feathers as the item in a to-do lists

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
