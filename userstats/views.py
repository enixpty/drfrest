from django.shortcuts import render
from expenses.models import Expense
from income.models import Income
import datetime
#django rest framework
from rest_framework import status, response
from rest_framework.views import APIView

#models 
from django.db.models import Sum

# Create your views here.
class ExpenseSummaryStats(APIView):

    def get_amount_for_category  (self,expense_list, category):
        expenses = expense_list.filter(category=category)
        #amount = 0 
        total_amount = expenses.aggregate(total=Sum('amount'))
    
        return { 'amount' :  str(total_amount['total'])}

    def get_category(self, expense):
        return expense.category

    
    def get(self, request):
        today_date = datetime.date.today()
        ayear_ago = today_date - datetime.timedelta(days=30*12) 
        expenses = Expense.objects.filter(
            owner=request.user , date__gte=ayear_ago, date__lte=today_date
        )

        final = {}
        categories = list(set(map(self.get_category, expenses)))

        for expense in expenses:
            for category in categories : 
                final[category] = self.get_amount_for_category(
                    expenses, category
                )
        return response.Response({'category_data' : final} , status=status.HTTP_200_OK)

    #income stats
class IncomeSummaryStats(APIView):

    def get_amount_for_source (self,income_list, category):
        income = income_list.filter(source=category)
        #amount = 0 
        total_amount = income.aggregate(total=Sum('amount'))
    
        return { 'amount' :  str(total_amount['total'])}

    def get_source(self, income):
        return income.source

    
    def get(self, request):
        today_date = datetime.date.today()
        ayear_ago = today_date - datetime.timedelta(days=30*12) 
        incomes = Income.objects.filter(
            owner=request.user , date__gte=ayear_ago, date__lte=today_date
        )

        final = {}
        sources = list(set(map(self.get_source, incomes)))

        for income in incomes:
            for source in sources : 
                final[source] = self.get_amount_for_source(
                    incomes, source
                )
        return response.Response({'source_data' : final} , status=status.HTTP_200_OK)