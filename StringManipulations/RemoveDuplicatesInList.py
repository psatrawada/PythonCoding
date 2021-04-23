#Remove duplicates in the list
#input:  [1,1,0,5,3,6,6,3,3,6,1,8]
#output:[1,0,5,3,6,8], [1,3,6]
def remDup(nums):
    dict = {}
    output = []
    ## creating unique list
    for x in nums:
        if(x in dict):
            dict[x] += 1
        else:
            dict[x] = 1
            output.append(x)
    ## creating duplicates list
    dups = []
    for i in dict:
        if(dict[i]>1):
            dups.append(i)
    return(output, dups)

def uniqList(nums):
    uniq = []
    for x in nums:
        if(x not in uniq):
            uniq.append(x)
    return(uniq)

input =  [1,1,0,5,3,6,6,3,6,1,8]
print("unique list and duplicates : ", remDup(input))
print("unique list only: ", uniqList(input))
