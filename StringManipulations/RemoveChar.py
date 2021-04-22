#Remove a characeter('L') from string
#input:  "HELLO WORLD"
#output:HEO WORD
def remchar(s):
    newstring = "";
    for i in s:
        if(i != 'l'):
            newstring += i ;
    return (newstring)

S = "Hello World"
print("Removed 'L' in a string: ", remchar(S) );
print("Remove 'o' in a string: ", S.replace('o', ""))
