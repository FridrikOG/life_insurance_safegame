from .serializers import InsuranceSerializer
from .models import Payment

def checkHasPaid(insurance):
    ins = InsuranceSerializer(insurance)
    payment = Payment.objects.filter(insurance=insurance)
    if not payment:
        return False
    return payment