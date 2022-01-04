from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.db.models import F
from core.models import Banci,Clienti,Asociere_Imprumuturi
from core.forms import BanciForm,ClientiForm,ImprumuturiForm

def welcome_page(request):
    query_asociere = Asociere_Imprumuturi.objects.filter(id__range=(170,210))
    banci = Banci.objects.all()
    clienti = Clienti.objects.all()
    #query_asociere = Asociere_Imprumuturi.objects.all()

    return render(request,'welcome.html', {'asociere' : list(query_asociere),'banci' : list(banci), 'clienti' : list(clienti)})



def create_menu(request):
    return render(request,'create_menu.html')

def create_banci(request):

    form = BanciForm()

    if request.method == 'POST':
        form = BanciForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form': form}
    return render(request,'create_banci.html',context)

def create_clienti(request):

    form = ClientiForm()

    if request.method == 'POST':
        form = ClientiForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form': form}
    return render(request, 'create_clienti.html',context)

def create_imprumuturi(request):

    form = ImprumuturiForm()

    if request.method == 'POST':
        form = ImprumuturiForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form': form}
    return render(request,'create_imprumuturi.html',context)




def read_menu(request):
    return render(request,'read_menu.html')

def read_banci(request):
    query_asociere = Banci.objects.all()
    return render(request,'read_banci.html', {'asociere' : list(query_asociere)})

def read_clienti(request):
    query_asociere = Clienti.objects.all()
    return render(request,'read_clienti.html', {'asociere' : list(query_asociere)})

def read_imprumuturi(request):
    #query_asociere = Asociere_Imprumuturi.objects.all()
    query_asociere = Asociere_Imprumuturi.objects.values('clienti__nume','banci__nume','suma')
    return render(request,'read_imprumuturi.html', {'asociere' : list(query_asociere)})



def update_menu(request):
    return render(request,'update_menu.html')

def update_banci(request,banca_id):
    banca_id =  Banci.objects.get(id = banca_id)
    banca_form = BanciForm(instance = banca_id)

    if request.method == "POST":
        banca_form = BanciForm(request.POST,instance = banca_id)
        if banca_form.is_valid():
            banca_form.save()
            return redirect('/')
    
        
    context = {'banca_form' : banca_form}
    return render(request,'update_banci.html',context)

def update_imprumuturi(request,imprumuturi_id):
    
    imprumuturi_id =  Asociere_Imprumuturi.objects.get(id = imprumuturi_id)
    imprumut_form = ImprumuturiForm(instance = imprumuturi_id)

    if request.method == "POST":
        imprumut_form = ImprumuturiForm(request.POST,instance = imprumuturi_id)
        if imprumut_form.is_valid():
            imprumut_form.save()
            return redirect('/')
    
        
    context = {'imprumut_form' : imprumut_form}
    return render(request,'update_imprumuturi.html',context)

def update_clienti(request,client_id):



    client_id =  Clienti.objects.get(id = client_id)
    client_form = ClientiForm(instance = client_id)

    if request.method == "POST":
        client_form = ClientiForm(request.POST,instance = client_id)
        if client_form.is_valid():
            client_form.save()
            return redirect('/')
    
        
    context = {'client_form' : client_form}
    return render(request,'update_clienti.html',context)




def delete_banci(request,banca_id):
    banca = Banci.objects.get(id = banca_id)

    if request.method=="POST":
        banca.delete()
        return redirect('/')

    context = {'banca' : banca}
    return render(request,'delete_banci.html',context)


def delete_clienti(request,client_id):
    client = Clienti.objects.get(id = client_id)

    if request.method=="POST":
        client.delete()
        return redirect('/')

    context = {'client' : client}
    return render(request,'delete_clienti.html',context)


def delete_imprumuturi(request,imprumut_id):
    imprumut = Asociere_Imprumuturi.objects.get(id = imprumut_id)

    if request.method=="POST":
        imprumut.delete()
        return redirect('/')

    context = {'imprumut' : imprumut}
    return render(request,'delete_imprumuturi.html',context)



















