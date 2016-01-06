from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items= Item.objects.all()

    return render(request, 'home.html', { 'items' : items, })

#home_page = None
# item = Item()
# item.text = request.POST.get('item_text', '')
# item.save()

    # remove: HttpResponse('<html><title>To-Do lists</title></html>') #test result = "false is not true"
    #render built into django
    #tell it which file we want to use
