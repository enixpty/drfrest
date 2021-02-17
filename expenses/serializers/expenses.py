from rest_framework import serializers

#model 
from expenses.models.expenses import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Expense
        fields = ['id','date','description','amount', 'category']