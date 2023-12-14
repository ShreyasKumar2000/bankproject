from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import login
from django.shortcuts import render, redirect




def home(request):
    return render(request, 'home.html')

#
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        c_password = request.POST.get('password2')

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('/register')
            else:
                cred = User.objects.create_user(username=username, password=password)
                cred.save()
        else:
            messages.info(request, "Passwords do not match")
            return redirect('/register')

        return redirect('/login')

    return render(request, "register_user.html")


def new_page(request):
    return render(request, 'new_page.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

# def forms(request):
#     return render(request, 'forms.html')
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AccountForm

def forms(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('lastpage'))
        else:
            print(form.errors)
    else:
        form = AccountForm()

    return render(request, 'forms.html', {'form': form})

def lastpage(request):
    return render(request, 'last.html')

from django.http import JsonResponse


def get_cities(request):
    CITIES_BY_DISTRICT = {
        'Alappuzha': ['Haripad','Kayamkulam','Cherthala','Alappuzha','Ambalappuzha'],
        'Ernakulam': ['Aluva', 'Ernakulam', 'Edapally', 'Vyttila', 'Muvattupuzha'],
        'Kollam': ['Karunagapally', 'Kollam', 'Oachira', 'Chavara', 'Kottarakara'],
        'Kozhikode': ['Vatakara', 'Koyilandi', 'Thamarassery', 'Kozhikode'],
        'Thiruvananthapuram': ['Kazhakootam', 'Trivandrum', 'Varkala', 'Kochuveli','Pettah'],
    }
    district = request.GET.get('district')
    cities = CITIES_BY_DISTRICT.get(district, [])
    return JsonResponse({'cities': cities})
