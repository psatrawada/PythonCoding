#Sum of a integer string
#input:  "2336754711"
#output: 15
def sumOfString(s):
    sum = 0
    for x in s:
        sum = sum + int(x)
    return(sum)
def sumByList(s):
    sum = 0
    stintlist = list(s)
    print(stintlist)
    for x in stintlist:
        sum += int(x)
    return(sum)
def sumByListRange(s):
    sum = 0
    stintlist = list(s)
    for x in range (len(stintlist)):
        sum += int(stintlist[x])
    return(sum)

input = "237111"
print("Sum Of String: ",  sumOfString(input))
print("Sum using list: ", sumByList(input))
print("Sum using list: ", sumByListRange(input))
