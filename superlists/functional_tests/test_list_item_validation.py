from unittest import skip
from .base import TodoFunctionalTest

class ItemValidationTest(TodoFunctionalTest):

    @skip("skip dis shit")
    def test_cannot_add_empty_list_item(self):
        #Edith goes to home page and accidentally tries
        #to submit an empty oilst item
        #she hits enter on the empty input box

        #the home page refreshes, and tehre is an error message
        #sayin ghta tlist items cannot be blank

        #she tries again with some text for the item
        #which now works

        #perversely tries to enter a second blank item

        #she receives a similar warining on the list page
        #and she can correct it by filling som etext in
        self.fail('Finish the fucking test Edith')
