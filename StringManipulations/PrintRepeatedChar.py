#Print repeated characeter from string
#input:  "HELLO WORLD"
#output: L, O
def repeatChar(s):
    repeats = {}
    for i in s:
        if i in repeats:
            repeats[i] += 1
        else:
            repeats[i] = 1
    return(repeats)

S = "Hello World"
#print("Repeated chars in a string: ", repeatChar(S) );
duplicates = repeatChar(S)
count = 0;
for key,value in duplicates.items():
    if(value > 1):
        print(key, " ")
        count +=1;
#print("There are " , count, " duplicate chars")
