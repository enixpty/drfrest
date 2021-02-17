""" users urls """

#django
from django.urls import path , include
from .views.user import RegisterView, VerifyEmail, LoginAPIView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("email-verify/", VerifyEmail.as_view(), name="email-verify")
]
