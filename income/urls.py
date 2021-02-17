
#django
from django.urls import path , include

from .views.income import IncomeListAPIView, IncomeDetailAPIView

urlpatterns = [
    path("", IncomeListAPIView.as_view(), name="incomes"),
    path("<int:id>", IncomeDetailAPIView.as_view(), name="income"),
  #  path("email-verify/", VerifyEmail.as_view(), name="email-verify")
]
