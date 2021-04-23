#Print repeated characeter from string
#input:  "HELLOOO WORLD"
#output: L, O
def repeatChar(s):
    repeats = {} #empty dictionary
    for i in s:
        if i in repeats:
            repeats[i] += 1
        else:
            repeats[i] = 1
    return(repeats)

def dupmaxchar(duplicates):
    max = 0;
    for k in duplicates:
        if(duplicates[k] > max):
            max = duplicates[k]
            ch = k
    return(ch, max)

S = "Helloooo World"
print("Repeated chars in a string: ", repeatChar(S) );
duplicates = repeatChar(S)
char,times = dupmaxchar(duplicates)
print("Character ",char,"appeared max",times,  " times")
