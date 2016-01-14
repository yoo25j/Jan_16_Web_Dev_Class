from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html', {'todo_lists': List.objects.all()})

def new_list(request):
    new_list = List.objects.create()
    item = Item(text=request.POST['item_text'], list=new_list)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        new_list.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error":error})
    return redirect('/lists/%d/' % (new_list.id,))

def view_list(request, list_id):
    list_ = List.objects.get(id = list_id)
    error = None

    if request.method == 'POST':
            if request.POST.has_key('item_text'):
                try:
                    item = Item(text = request.POST['item_text'], list = list_)
                    item.full_clean()
                    item.save()
                except ValidationError:
                    error = "You can't have an empty list item"
            if request.POST.has_key('list_name'):
                list_.name = request.POST['list_name']
                list_.save()

    return render(
        request, 'list.html',
        { 'list': list_, 'error': error}
    )

def edit_list (request, list_id):
    list_= List.objects.get(id=list_id)
    for item in list_.item_set.all():
        item.is_done = False
        item.save()
    item_ids = request.POST.getlist('mark_item_done')
    for item_id in item_ids:
        item= Item.objects.get(id=item_id)
        item.is_done = True
        item.save()
    return redirect('/lists/%d/' % (list_.id))
