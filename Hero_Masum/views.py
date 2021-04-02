from django.shortcuts import render
from django.http import HttpResponse
from .models import Item,ToDoList
from datetime import date

# Create your views here.

def index(response):
    return HttpResponse("<h1>Masum Bhai is Hero</h1>")
def anything(response,id):
    ls = ToDoList.objects.get(id=1); #Here is the trick i am using
    #item = ls.item_set.get(id=1);

    t = date.today()
    month = date.strftime(t, '%b')
    year = t.year
    tarikh = " %s-%s" % (month, year)
    return HttpResponse("<h1>Love You Masum 😍 (me to myself (¬‿¬)</h1>"
                        f"<h2>Hey id: {id}</h2>"
                        f"<h2>{ls.name} for {tarikh} :</h2>"
                        #f"<p><h4>{str(item.text)}</h4></p>"
                        )

def urlError(response,id):
    return HttpResponse(f"<h1>Yo Bro,this {id} page is not Present right Now.</h1>")


