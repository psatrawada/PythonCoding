#merge lists and remove duplicates
#input1:[1,0,5,3,7,13,2],input2 [1,3,5,2,5,11]
#ouput: [0,1,2,3,5,7,11,13]

def merge2List(in1,in2):
    output = []
    for x in in1:
        for y in in2:
            if(x not in output):
                output.append(x)
            if(y not in output):
              output.append(y)
        output.sort()
    return(output)

input1 = [1,0,5,3,7,13,2]
input2 = [1,3,5,2,5,11]
print("Merged List: ", merge2List(input1, input2))
