from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-form", views.createForm, name="create-form"),
    path("display-forms", views.displayForms, name="display-forms"),
    path("update-form/<int:claimId>", views.updateForm, name="update-form"),
    path("delete-form/<int:claimId>", views.deleteForm, name="delete-form"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout")
]
