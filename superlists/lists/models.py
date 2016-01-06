from django.db import models

class Item(models.Model): #models.Model leverages django to give us save method
    text = models.TextField(default = '') #value empty string is reasonable bc its a text field,
    #pass
