from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .forms import *
import random


# Create your views here.
class HomeView(View):
    def get(self, request):
        return TemplateResponse(request, 'home.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('user', args=[user.id]))
            else:
                return HttpResponse('Niepoprawne dane logowania!')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'createUser.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            new_User = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,

            )
        return HttpResponseRedirect(reverse('login'))


class ProfilView(View):
    def get(self, request):
        random = request.user
        return render(request, 'profil.html', {"user": random})


class AddMoneyView(View):
    def get(self, request):
        form = MoneyForm()
        id = request.user.id
        return render(request, 'addMoney.html', {'form': form, 'id': id})

    def post(self, request):
        form = MoneyForm(request.POST)
        id = request.user.id
        user = User.objects.get(id=id)
        if form.is_valid():
            value = int(form.cleaned_data["value"])
            user.money += value
            user.save()
            return HttpResponseRedirect(reverse('user'))


class CaseView(View):
    def get(self, request):
        case = Case.objects.all()
        return TemplateResponse(request, 'case.html', {"cases": case})


class CaseDetailsView(View):
    def get(self, request, pk):
        case = Case.objects.get(pk=pk)
        items = case.item_list.all()
        return TemplateResponse(request, 'caseDetails.html', {"items": items})

    def post(self, request, pk):
        case = Case.objects.get(pk=pk)
        if request.user.money < case.price:
            return HttpResponse("nie stac cie hahhahahahaha")
        items = case.item_list.all()
        object_list = range(len(items))
        random.shuffle(object_list)
        loss = object_list[0]
        request.user.item.add(items[loss])
        request.user.money -= case.price
        request.user.save()
        print(request.user.money)
        return HttpResponseRedirect(reverse('inventory'))


class InventoryView(View):
    def get(self, request):
        items = request.user.item.all()
        return TemplateResponse(request, 'inventory.html', {"items": items})
