import math as m
import numpy as np
''' include the proper directory of the file'''
 
f=open('C:\\Users\\user\\Desktop\\important\\csv\\sales.csv','r')
w=[]
q=[]
e=f.read().splitlines()


''' CHANGE THE NUMBER WITHIN  THIRD BRACKETS FOR APPROPRIATE VALUE OF INDEPENDENT VARIABLE AND DEPENDENT VARIABLES '''


for i in range(1,len(e)):
    n=e[i]
    z=n.split(',')
    
    w.append(z[8])  
    q.append(z[13])

sum=0
sum1=0
''' MEANX'''
for i in w:
    sum+=float(i)
size=np.size(w)
print('meanx')
print('-'*46)
meanx=sum/size
print(meanx)
'''MEANY'''
for i in q:
    sum1+=float(i)
print('meany')
print('-'*46)
meany=sum1/size
print(meany)
print('-'*46)

for i in range(2):
    m1=0
    m2=0
    for i,j in zip(w,q):
        a=(float(i)-meanx)*(float(j)-meany)
        b=m.pow((float(i)-meanx),(2))
        m1=m1+a
        m2+=b
    break

m=m1/m2
print("THE VALUE OF 'M' IS")
print(float(m))
c=((meany)-((meanx)*(float(m))))
print("THE VALUE OF 'C' IS")
print(c)
print('-'*46)
y=[]

for j in range(2):
    for i in w:
        r=(m)*float(i)+float(c)
        y.append(r)
    print(y)
    break



'''   DATA  TESTING'''



print('-'*46)
print('  TESTING DATA')

h=int(input('enter the number of points'))
k=[]
for i in range(h):
    k.append(float(input(' enter point')))
    
for i in k:
    print('MY ASSUMPTIONS TO THE REQUEST IS....')
    print((m)*float(i)+float(c))


'''  COST FUNCTION'''



print('-'*46)
print('  COST FUNCTION')


m=5
sum2=0
for i,j in zip(y,q):
    s=i-float(j)
    c=np.power(s,2)
    sum2+=c
j=sum2/(2*m)
print(j)



    



