from django.shortcuts import render
from .models import User

# Create your views here.
#request -> parametro imbutido no django que permite acessar os dados que estao dentro da pagina
def Home(request):
    return render(request, 'users/home.html')

def Users(request):
    # salvando os dados no BD
    new_user = User()
    new_user.name = request.POST.get('user_name')
    new_user.age = request.POST.get('user_age')
    new_user.save()

    # listando os usuarios
    users_list = {
        'users': User.objects.all()
    }

    # retornando os dados para a pagina de listagem

    return render(request, 'users/users.html', users_list)
