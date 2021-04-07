from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, ToDoList
from datetime import date


# Create your views here.

def anything(response, id):
    ls = ToDoList.objects.get(id=1);  # Here is the trick i am using
    # item = ls.item_set.get(id=1);

    t = date.today()
    month = date.strftime(t, '%b')
    year = t.year
    tarikh = " %s-%s" % (month, year)
    # return HttpResponse("<h1>Love You Masum 😍 (me to myself (¬‿¬)</h1>"
    #                     f"<h2>Hey id: {id}</h2>"
    #                     f"<h2>{ls.name} for {tarikh} :</h2>"
    #                     # f"<p><h4>{str(item.text)}</h4></p>"
    #                     )
    return render(request=response,
                  template_name='Hero_Masum/base.html',
                  context={"todo_name":ls.name})


def urlError(response, id):
    return HttpResponse(f"<h1>Yo Bro,this {id} page is not Present right Now.</h1>")


def index(response,id):
    ls = ToDoList.objects.get(id=1);  # Here is the trick i am using
    return render(response, "Hero_Masum/todoList.html", {"ls":ls})


def home(response):
    return render(response, "Hero_Masum/home.html", {})
