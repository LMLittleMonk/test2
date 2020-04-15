from django.shortcuts import render,redirect
from booktest.models import *
from datetime import date
# Create your views here.
#显示图书列表
def index(request):
    booklist=BookInfo.objects.all()
    return render(request,'booktest/index.html',{'booklist':booklist})
#点击这本书显示这本书里所有的英雄

def detail(request,bid):
    # select * from HeroInfo where hid = 1
    book = BookInfo.objects.get(id=int(bid))
    heros = book.heroinfo_set.all()
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})

def index2(request):
    list = BookInfo.objects.all()
    return render(request, 'booktest/index2.html', {'list': list})

def create(request):
    book = BookInfo()
    book.btitle = '天涯明月刀'
    book.bpub_date = date(1992,2,4)
    book.save()
    return redirect('/list')
def delete(request,id):
    book = BookInfo.objects.get(id =int(id))
    book.delete()
    return redirect('/list')
