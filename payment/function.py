from .serializers import InsuranceSerializer
from .models import Payment
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

def checkHasPaid(insurance):
    ins = InsuranceSerializer(insurance)
    payment = Payment.objects.filter(insurance=insurance)
    if not payment:
        return False
    return payment


def getAge(dob):
    print("Inside dob ", dob)
    print("Dob ")
    
    age = dob - datetime.now(timezone.utc)
    today = datetime.now(timezone.utc)
    print("The age ", age )
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    print("Current age ", age )
    return age


def getYearFromNow():
    expiryOfInsurance = datetime.now(timezone.utc)
    expiryOfInsurance = datetime.strptime(str(expiryOfInsurance), "%Y-%m-%d")
    return expiryOfInsurance