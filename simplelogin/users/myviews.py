from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm
from .models import User


@login_required
def list_allusers(request):
    users = User.objects.all()
    print(users)
    return render(request, "my_users/list_all.html", {"users": users})


class LoginView(View):
    template_name = "my_users/login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        print("jjj")
        form = self.form_class()
        return render(request=request, template_name=self.template_name, context={"form": form})

    def post(self, request):
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("users:detail", pk=user.id)
        else:
            messages.error(request, "username or password not correct")
            return redirect("users:login")


login_view = LoginView.as_view()
