from django.shortcuts import render

# Create your views here.
def all_products(request):
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            if 'tech' in categories:
                return render(request, 'products/tech_products.html')
            if 'appliances' in categories:
                return render(request, 'products/appliances.html')

    return render(request, 'products/products.html')
