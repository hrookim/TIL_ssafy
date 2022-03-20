from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    fruits = ['apple', 'banana', 'kiwi', 'mango']
    context = {
        'name': 'Alice',
        'fruits': fruits,
    }
    return render(request, 'articles/greeting.html', context)