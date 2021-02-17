from rest_framework import serializers

#model 
from income.models.income import Income

class IncomeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Income
        fields = ['id','date','description','amount', 'source']