#Reverse a string
#input:  "HELLO World"
#output: dlroW olleH

def rev(s):
    newstring = "";
    for i in s:
        newstring = i + newstring;
    return (newstring)

def revRecursive(s):
    if len(s)== 0 :
        return(s)
    else:
        return (revRecursive(s[1:]) + s[0])


S = "Hello World"
print(S, "is reversed as ", rev(S) );
print(S, "is reversed using recursive ", revRecursive(S) );
