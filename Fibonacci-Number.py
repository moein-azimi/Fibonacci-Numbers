A = [1,1]
n = input("number: ")
for i in range(0,int(n)):
    m = A[i]+A[i+1]
    A.append(m)    
print(A)    
