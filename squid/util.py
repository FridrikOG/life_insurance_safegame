from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta


def getYearFromNow():
    expiryOfInsurance = datetime.now(timezone.utc) + relativedelta(years=1)
    expiryOfInsurance = expiryOfInsurance.strftime("%Y-%m-%d")
    expiryOfInsurance = datetime.strptime(str(expiryOfInsurance), "%Y-%m-%d")
    return expiryOfInsurance