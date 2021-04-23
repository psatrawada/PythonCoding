#input:  [0,12,1,4,2,3,0]
#output: 0,12
def smallestLargestNum(nums):
    n = len(nums);
    s = nums[0];
    l = nums[0];
    for i in range (n):
        if(nums[i] < s):
            s = nums[i]
        if(nums[i] > l):
            l = nums[i]
    return(s,l)

input = [12,1,4,452,3,0,3]
S, L = smallestLargestNum(input)
print("Smallest=",S, " Largest=",L)
