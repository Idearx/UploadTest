from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'common/huawei.html')


def detail(request):
    return render(request,'common/phone_base_detail.html',context={
        'title':'华为P30',
    })


def shopping_car(request):
    return render(request, 'common/shopping_car.html', context={
        'title':'购物车'
    })