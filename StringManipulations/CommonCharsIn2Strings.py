# I/P: (string, strong) O/P: strng

Input1 = "String"
Input2 = "Strong"

def CommonCharsInString(st1, st2):
    output = ""
    for i in st1:
        for j in st2:
            if(i == j):
                output += i            
    return(output)

print("Common chars of 2 strings is: ",CommonCharsInString(Input1,Input2))
