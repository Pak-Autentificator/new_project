from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

#-----------------------------------------------------------------------------------------

from .forms import RegistrationForm
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Аутентификация пользователя
            authenticated_user = authenticate(request, username=user.username, password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')  # Перенаправьте пользователя на главную страницу
            else:
                # Обработка ошибки аутентификации (например, неверные учетные данные)
                # Добавьте свой код обработки ошибки здесь
                pass
    else:
        form = RegistrationForm()

    return render(request, 'register/register.html', {'form': form})

#-----------------------------------------------------------------------------------------

from django.contrib.auth import login
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})

#-----------------------------------------------------------------------------------------