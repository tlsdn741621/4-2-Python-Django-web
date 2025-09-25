from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger


def main(request):
    # return HttpResponse("Hello, world. 파이버거~~")
    return render(request, 'main.html')

def burger_list(request):
    # return HttpResponse("파이버거의 햄버거 목록입니다.~~~")
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:", burgers)
    context = {'burgers': burgers}
    return render(request, 'burger_list.html', context)