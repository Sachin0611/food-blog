from multiprocessing import context
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import  HttpResponse
from food.models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
           'item_list' : item_list,
    }
    return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
def item(request):
    return HttpResponse("This is an item!")

class foodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'

def detail(request, item_id):
        item = Item.objects.get(pk=item_id)
        context = {
            'item':item,
        }
        return render(request,'food/detail.html',context)

class createview(CreateView):
    model = Item
    template_name = 'food/item-form.html'
    fields = ['item_name','item_desc','item_price','item_image']

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
       instance = form.save()
       instance.user_name = request.user
       instance.save()
       return redirect("/food/")


    return render(request,'food/item-form.html',{'form':form})

def update_item(request,item_id):
     item = Item.objects.get(pk=item_id)
     form = ItemForm(request.POST or None,instance=item)

     if(form.is_valid()):
        form.save()
        return redirect("/food/")

     return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,item_id):
    item = Item.objects.get(pk=item_id)

    if request.method == "POST":
        item.delete()
        return redirect("/food/")

    return render(request, "food/item-delete.html", {'item':item})
          