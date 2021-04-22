#Product of List of integers
#input:  [0,2,1,4,2,3]
#output:

def LargesProdOf2(nums):
    prod2 = nums[0]*nums[1]
    n = len(nums)
    for x in range (n-1):
        if(nums[x]*nums[x+1]>prod2):
            prod2 = nums[x]*nums[x+1]
    return(prod2)

def LargesProdOf3(nums):
    prod3 = nums[0]*nums[1]*nums[2]
    n = len(nums)
    for x in range (n-2):
        if(nums[x]*nums[x+1]*nums[x+2]>prod3):
            prod3 = nums[x]*nums[x+1]*nums[x+2]
    return(prod3)

input = [0,12,1,4,2,3,0]
print("Largest product of 2 consecutive integers: ", LargesProdOf2(input))
print("Largest product of 3 consecutive integers: ", LargesProdOf3(input))
