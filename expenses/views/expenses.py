#django REST framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
#serializer
from expenses.serializers.expenses import ExpenseSerializer

#models
from expenses.models import Expense

#permisions 
from expenses.permissions import IsOwner

class ExpenseListAPIView(ListCreateAPIView): 
    """ list expense view """
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = ( IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    

class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView): 
    """ list expense view """
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = ( IsAuthenticated, IsOwner)
    lookup_field = 'id'

    #def perform_create(self, serializer):
     #   return serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    



