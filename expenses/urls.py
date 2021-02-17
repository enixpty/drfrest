
#django
from django.urls import path , include

from .views.expenses import ExpenseListAPIView, ExpenseDetailAPIView

urlpatterns = [
    path("", ExpenseListAPIView.as_view(), name="expenses"),
    path("<int:id>", ExpenseDetailAPIView.as_view(), name="expense"),
  #  path("email-verify/", VerifyEmail.as_view(), name="email-verify")
]
