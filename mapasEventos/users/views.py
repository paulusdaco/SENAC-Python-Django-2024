from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')  # Redireciona para a página inicial após o logout
    # Se for GET, pode redirecionar para onde achar adequado, ou exibir uma mensagem de erro

    # Caso precise de uma resposta para um método diferente de POST:
    return redirect('index')
