from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Bumi',
        'author': 'Tere Liye',
        'price': '90000',
        'amount': '100',
        'description': 'Novel'
    }

    return render(request, "main.html", context)