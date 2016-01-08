from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html', )

def new_list(request):
    new_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=new_list)
    return redirect('/lists/%d/' % (new_list.id,))

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items= Item.objects.filter(list=list_)
    return render(
        request, 'list.html',
        { 'items' : items, 'list' : list_,})

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_,)
    return redirect('/lists/%d/' % (list_.id,))


#home_page = None
# item = Item()
# item.text = request.POST.get('item_text', '')
# item.save()

    # remove: HttpResponse('<html><title>To-Do lists</title></html>') #test result = "false is not true"
    #render built into django
    #tell it which file we want to use
