from django.shortcuts import render

# Create your views here.


def cart(request):
    return render(request, 'fourth_task/index.html', {'games': ['Atomic Heart', 'Cyberpunk 2077']})

def game(request):
    items = {
        'item1': 'Игровая приставка',
        'item2': 'Игра 1',
        'item3': 'Игра 2',
    }
    return render(request, 'fourth_task/store.html', {'items': items})

def platform(request):
    return render(request, 'fourth_task/cart.html')


