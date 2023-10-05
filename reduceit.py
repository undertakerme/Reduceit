n=input("enter list")#reduceit
x=n.split()
y=[]
z=[]
for i in range(len(x)):
     y.append(int(x[i]))
print (y)
r=len(y)
for j in range(r-1):
     if((y[j]!=y[j+1])and(y[j]<y[j+1])):
          continue
     elif(y[j]>y[j+1]):
          y[j],y[j+1]=y[j+1],y[j]
     else:
          y[j+1]=2*int(y[j])
          y[j]=0
for i in range(len(y)):
    if(y[i]==0):
       continue
    else:
       z.append(y[i])
print("final list will be",z)
