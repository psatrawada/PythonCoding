#Fibnocci {0,1,2,3,5,8,13,21,34,55..}
#Find Fib for n digit
def recur_fibo(n):
    if(n <= 1):
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def recur_fiboseries(n):
 flist = []
 for i in range(n+1):
     fib = recur_fibo(i)
     flist.append(fib)
 return(flist)

n=20
print(" Fibnocci Series : ",recur_fiboseries(n))
print(" Fibnocci nth digit: ",recur_fibo(n))
