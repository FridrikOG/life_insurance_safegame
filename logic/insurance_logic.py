import pandas as pd
import numpy  as np

mortalityTable=pd.read_csv('MortalityTable.csv',sep=';')
mortalityTable.head()

riskLoads=pd.read_csv('RiskLoads.csv',sep=';')
riskLoads.head()
riskLoads


cover_amount=2500000 
#Base rate determined by competitor analysis
base_rate=0.01

mortalityTable['ExpectedLossMale']=mortalityTable['Male_Hazard_Rate']*cover_amount
mortalityTable['ExpectedLossFemale']=mortalityTable['Female_Hazard_Rate']*cover_amount
mortalityTable.head()


def get_rate(age,gender,factors):

    if gender=='male':
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Male_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossMale'].values[0]
        
    else:
        #hazardRate=mortalityTable.loc[mortalityTable.Age == age,'Female_Hazard_Rate'].values[0]
        expectedLoss=mortalityTable.loc[mortalityTable.Age == age,'ExpectedLossFemale'].values[0]
    
    for i in factors:
        print(i)
        RiskLoad=riskLoads.loc[riskLoads.Factor== i,'RiskLoad'].values[0]
        RiskLoad_adjusted=RiskLoad*expectedLoss
        expectedLoss+=RiskLoad_adjusted

    
    # Yearly Premium as a percentage of cover amount
    TotalRate=base_rate+(expectedLoss/cover_amount)

    # Yearly premium (Expected loss+variable risk)
    Annual_Premium=(base_rate*cover_amount)+expectedLoss

    print('Your Annual Premium is:')


     


  
    return Annual_Premium

john=get_rate(24,'male',['Smoker','CarOwner'])
print(john)