from django.shortcuts import render

def categories_list(request):
    return render(request, 'categories/categories_list.html')