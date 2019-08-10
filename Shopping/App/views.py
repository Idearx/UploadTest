from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'common/huawei.html')


def detail(request):
<<<<<<< HEAD
    return render(request,'common/detailnew2.html',context={
=======
    return render(request,'common/phone_base_detail.html',context={
>>>>>>> origin/master
        'title':'华为P30',
    })


<<<<<<< HEAD
def login(request):
    return render(request,'common/hualogin.html',context={
        'title':'为华-登录'
=======
def shopping_car(request):
    return render(request, 'common/shopping_car.html', context={
        'title':'购物车'
>>>>>>> origin/master
    })