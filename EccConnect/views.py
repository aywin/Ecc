
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Eleve

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



# Create your views here.




def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger l'utilisateur vers la page de destination après la connexion
            return redirect('home')  # Changez 'home' avec le nom de la vue ou l'URL désirée
        else:
            # Gérer le cas où l'authentification échoue
            pass  # Vous pouvez ajouter une logique pour afficher un message d'erreur à l'utilisateur
    return render(request, 'EccConnect/login.html')

# Exemple de vérification du type d'utilisateur après la connexion




# Vue pour la page d'accueil
@login_required
def home(request):
    if request.user.is_superuser:
        # Afficher des fonctionnalités administratives pour les superutilisateurs
        print("L'utilisateur est un superutilisateur")
        return render(request, 'EccConnect/home.html')

    elif request.user.groups.filter(name='Alumni').exists():
        # Afficher des fonctionnalités spécifiques aux alumni
        print("L'utilisateur est un alumni")
        return render(request, 'EccConnect/home.html')

    elif request.user.groups.filter(name='Eleve').exists():
        # Afficher des fonctionnalités spécifiques aux élèves
        print("L'utilisateur est un élève")
        return render(request, 'EccConnect/home.html')

    else:
        print("L'utilisateur n'est ni un superutilisateur ni un alumni ni un élève")
        return render(request, 'EccConnect/home.html')
def index(request):
    mem=Eleve.objects.all()
    return render(request, 'EccConnect/index.html', {'mem':mem})


def add(request):
    return render(request, 'EccConnect/add.html')




def addrec(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        x= request.POST['first']
        y = request.POST['first']
        z = request.POST['first']
        mem=Eleve(firstname=x, lastname=y,  password=z)
        mem.save()
        return redirect('index')
        
def delete(request,id):
    mem=Eleve.objects.get(id=id)
    mem.delete()
    return redirect('index')

def update(request,id):
    mem=Eleve.objects.get(id=id)
    return render(request, 'EccConnect/update.html',{'mem':mem})

def uprec(request,id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        x= request.POST['first']
        y = request.POST['last']
        z = request.POST['password']
        mem=Eleve.objects.get(id=id)
        mem.firstname=x
        mem.lastname=y
        mem.password=z
        mem.save()
        return redirect('index')