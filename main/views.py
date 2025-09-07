from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406355136',  # Ubah sesuai dengan npm kamu
        'name': 'Bisma Zharfan SW',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
