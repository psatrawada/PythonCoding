#Print quotient and reminder of a given 2 nums
#input:  (25,4)
#output:6,1
def twoGiven(n1,n2):
    q = n1//n2
    r = n1%n2
    return(q,r)
print("Quotient and reminder (25,4): ", twoGiven(25,4))
