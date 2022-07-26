
COVER_MULTIPLIER=250000
COVER_AMOUNT = 250000*10
BASE_RATE=0.01
import pandas as pd
import numpy as np
# Create your views here.
def getTables():

    
    
    mortalityTable=pd.read_csv('insurance/MortalityTable.csv',sep=';')
    mortalityTable.head()
    riskLoads=pd.read_csv('insurance/RiskLoads.csv',sep=';')
    riskLoads.head()
    riskLoads
    mortalityTable['ExpectedLossMale']=mortalityTable['Male_Hazard_Rate']*COVER_MULTIPLIER
    mortalityTable['ExpectedLossFemale']=mortalityTable['Female_Hazard_Rate']*COVER_MULTIPLIER
    mortalityTable.head()
    return mortalityTable, riskLoads

def getRate(age,gender = 'male',factors = []):
    mortalityTable, riskLoads = getTables()
    if gender=='male':
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Male_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossMale'].values[0]
    else:
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Female_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossFemale'].values[0]
    for x in factors:
        try:
            RiskLoad=riskLoads.loc[riskLoads.Factor== x,'RiskLoad'].values[0]
            RiskLoad_adjusted=RiskLoad*expectedLoss
            expectedLoss+=RiskLoad_adjusted
        except:
            print("Error ")
    # Yearly Premium as a percentage of cover amount
    TotalRate=BASE_RATE+(expectedLoss/COVER_MULTIPLIER)
    # Yearly premium (Expected loss+variable risk)
    Annual_Premium=(BASE_RATE*COVER_MULTIPLIER)+expectedLoss
    return int(Annual_Premium)

def getCoverAmount():
    return COVER_AMOUNT