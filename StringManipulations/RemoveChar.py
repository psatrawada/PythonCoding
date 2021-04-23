#Remove a characeter('L') from string
#input:  "PYTHONWORLD"
#output:HEO WORD
def remchar(s):
    newstring = ""
    for i in s:
        if(i != 'l'):
            newstring += i ;
    return (newstring)

def removeIndex(s, n):
    upToIndex = s[:n]
    afterIndex = s[n+1:]
    newString = upToIndex + afterIndex
    return(newString)

S = "PYTHON WORLD"
print("Removed 'L' in a string: ", remchar(S) );
print("Remove 3rd index in a string: ", removeIndex(S, 3))
print("Remove 'O' in a string: ", S.replace('O', ""))
