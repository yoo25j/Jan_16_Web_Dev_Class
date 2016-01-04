from selenium import webdriver
# write test first before writing the program
# Edith has heard abot a call new online to-do app
# She goes to check out its homepage
browser = webdriver.Firefox()
#start a portal 8000
#go to the homepage
browser.get('http://localhost:8000')
# She notices the page title and header mention to-do lists.
assert 'Django' in browser.title

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
browser.quit()
