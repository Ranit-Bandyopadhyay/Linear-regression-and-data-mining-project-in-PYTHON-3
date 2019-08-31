''' Comparing the ratio of total profit to the units sold for each region  '''


import numpy as np
''' include the proper directory of the file'''
 
f=open('C:\\Users\\user\\Desktop\\important\\csv\\sales.csv','r')
w=[]
q=[]
SS=[]
AO=[]
CC=[]
EU=[]
A=[]
MEA=[]
e=f.read().splitlines()

for i in range(1,len(e)):
    t=e[i].split(',')
    w=t[8]
    q=t[13]
    x=t[0]
    if(x=='Sub-Saharan Africa'):
        SS.append(float(q)/float(w))
    elif(x=='Australia and Oceania'):
        AO.append(float(q)/float(w))
    elif(x=='Central America and the Caribbean'):
        CC.append(float(q)/float(w))
    elif(x=='Europe'):
        EU.append(float(q)/float(w))
    elif(x=='Asia'):
        A.append(float(q)/float(w))
    else:
        MEA.append(float(q)/float(w))
    
meanSS=np.mean(SS)
meanAO=np.mean(AO)
meanCC=np.mean(CC)
meanEU=np.mean(EU)
meanA=np.mean(A)
meanMEA=np.mean(MEA)

if(meanSS>meanAO and meanSS>meanCC and meanSS>meanEU and meanSS>meanA and meanSS>meanMEA):
    print(meanSS)

elif(meanAO>meanSS and meanAO>meanCC and meanAO>meanEU and meanAO>meanA and meanAO>meanMEA):
    print(meanAO)
        
elif(meanCC>meanSS and meanCC>meanAO and meanCC>meanEU and meanCC>meanA and meanCC>meanMEA):
    print(meanCC)
        
elif(meanEU>meanSS and meanEU>meanAO and meanEU>meanCC and meanEU>meanA and meanEU>meanMEA):
    print(meanEU)
        
elif(meanA>meanSS and meanA>meanCC and meanA>meanEU and meanA>meanAO and meanA>meanMEA):
    print(meanA)
else:
    print(meanMEA)
        
    
    
        
    

        