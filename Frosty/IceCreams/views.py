from django.shortcuts import render, redirect

from IceCreams.models import Flavour

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        id = request.POST.get('id')
        launched_on = request.POST.get('date')
        vegan = request.POST.get('vegan')
        if vegan == "on":
            vegan = True
        else:
            vegan = False
        location = request.POST.get('location')        
        limited = request.POST.get('limited')
        if limited == "on":
            limited = True
        else:
            limited = False
        customers = request.POST.get('customers')
        flavour = Flavour(name=name, id=id, launched_on = launched_on, vegan_available = vegan, location=location, limited_edition=limited, customers = customers)
        flavour.save()
    info = Flavour.objects.all()
    return render(request, 'home.html', {'info':info})

def add(request):
    return render(request, 'add.html')

def update(request, pk):
    if request.method == "POST":
        flavour = Flavour.objects.get(id=pk)
        flavour.name = request.POST.get('name')
        flavour.launched_on = request.POST.get('date')
        vegan = request.POST.get('vegan')
        if vegan == "on":
            flavour.vegan = True
        else:
            flavour.vegan = False
        flavour.location = request.POST.get('location')        
        limited = request.POST.get('limited')
        if limited == "on":
            flavour.limited = True
        else:
            flavour.limited = False
        flavour.customers = request.POST.get('customers')
        flavour.save()
        return redirect('/')
    flavour = Flavour.objects.get(id=pk)
    date_str = str(flavour.launched_on)
    flavour.launched_on = date_str
    return render(request, 'update.html', {'flavour':flavour})

def delete(request, pk):
    flavour = Flavour.objects.get(id=pk)
    flavour.delete()
    return redirect('/')

    