from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth

from .forms import ClaimModelForm, UserRegisterForm, UserLoginForm
from .models import ClaimsModel

# Create your views here.


def home(request):
    claimsList = ClaimsModel.objects.all()
    context = {}
    context["numOfClaimsList"] = claimsList.count()
    context["numIsPoliceReported"] = ClaimsModel.objects.filter(
        isPoliceReported="Yes").count()
    context["numIsInjured"] = ClaimsModel.objects.filter(
        isInjured="Yes").count()
    return render(request, "claims/home.html", context)


def displayForms(request):
    if request.user.is_authenticated:
        claimsList = ClaimsModel.objects.filter(owner=request.user)
        context = {}
        context["claimsList"] = claimsList
        context["numOfClaimsList"] = claimsList.count()
        return render(request, "claims/displayForms.html", context)
    else:
        return render(request, "claims/displayForms.html")


def createForm(request):
    form = ClaimModelForm()
    if request.method == "POST":
        # print("Payload: ", request.POST)
        form = ClaimModelForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)  # save into db
            obj.owner = request.user
            obj.save()
            return redirect("/display-forms")

    context = {"form": form}
    return render(request, "claims/claimsForm.html", context)


def updateForm(request, claimId):
    claim = ClaimsModel.objects.get(id=claimId)
    form = ClaimModelForm(instance=claim)
    if request.method == "POST":
        form = ClaimModelForm(request.POST, request.FILES, instance=claim)

        if form.is_valid():
            obj = form.save(commit=False)  # save into db
            obj.owner = request.user
            obj.save()
            return redirect("/display-forms")
    # redirect to single updated object
    context = {"form": form}
    return render(request, "claims/claimsForm.html", context)


def deleteForm(request, claimId):
    claim = ClaimsModel.objects.get(id=claimId)
    if claim != None:
        claim.delete()

    return redirect("/display-forms")


def register(request):
    regForm = UserRegisterForm()
    if request.method == "POST":
        regForm = UserRegisterForm(request.POST)

        if regForm.is_valid():
            username = regForm.cleaned_data.get("username")
            password1 = regForm.cleaned_data.get("password1")
            password2 = regForm.cleaned_data.get("password2")

            # verify password
            if password1 == password2:
                # verify for duplicate username in db
                isDuplicated = User.objects.filter(username=username).exists()
                if isDuplicated:
                    messages.info(request, "Username already taken!")
                    redirect("/register")
                else:
                    user = User.objects.create_user(
                        username=username, password=password1)
                    user.save()
                    return redirect('/login')
            else:
                messages.info(request, "Password not matching!")
                redirect("/register")
    context = {"regForm": regForm}
    return render(request, 'claims/register.html', context)


def login(request):
    loginForm = UserLoginForm()
    if request.method == "POST":
        loginForm = UserLoginForm(request.POST)

        if loginForm.is_valid():
            username = loginForm.cleaned_data.get("username")
            password = loginForm.cleaned_data.get("password")

            # verify for user records in db
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Wrong username/password!")
                return redirect("/login")

    context = {"loginForm": loginForm}
    return render(request, 'claims/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect("/")
