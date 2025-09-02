from django.shortcuts import render

#from django.shortcuts import render

def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def products(request):
    return render(request, "main/products.html")

def contact(request):
    return render(request, "main/contact.html")

def heavy_duty_grid(request):
    return render(request, 'main/heavy_duty_grid.html')

def light_grid(request):
    return render(request, 'main/light_grid.html')

def nestable(request):
    return render(request, 'main/nestable.html')

def light_flat(request):
    return render(request, 'main/light_flat.html')

def flat_top_heavyduty(request):
    return render(request, 'main/flat-top-heavyduty.html') 


# Create your views here.








