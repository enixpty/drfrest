#django REST framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
#serializer
from income.serializers.income import IncomeSerializer

#models
from income.models import Income

#permisions 
from expenses.permissions import IsOwner

class IncomeListAPIView(ListCreateAPIView): 
    """ list expense view """
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = ( IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    

class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView): 
    """ list expense view """
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = ( IsAuthenticated, IsOwner)
    lookup_field = 'id'

    #def perform_create(self, serializer):
     #   return serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    



