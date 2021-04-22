print ("Hello world");
print ('Hello Hello');
print("print range of numbers in for loop: ")
for x in range(4):
    print(x)
print("End of For loop")
nums = [7,11,13,17]
for i in nums:
    print(i)
print("End of For loop")

print("print chars using For loop: ")
str = "python"
for i in str:
    print(i)
st1 = "Loop"
for i in range (len(st1)):
    print(st1[i])

print("print chars using slicing: ")
str1 = "count"
print("length of String: ", len(str1))
print("Find index of a char 'c': ", str1.find('c')) #finds the first occurence
print(str1[:] +" " +str1[:5])
print("1st_Last_char: ", str1[0]+ str1[-1])
print("firstandLast: ", str1[:1] + str1[4:] )
print("Last_3_chars: ", str1[-3:])
print("In_between_1st_last chars: ", str1[1:4] )


print("RepeatAString 5 time", str1*5)
str2 = str1*3
print("Replace a char: ", str2.replace('c','xx', 2), str2.replace('o', 'yy'), str2.replace('n',""))
print("str1 and str2: ", str1+str2)

str3 = "2345678"
strToCharsList = list(str3)
print(strToCharsList)

text1 = "44count44 count44 strip5644 "
print("Split a string: ", text1.split('44'))
list1 = text1.split('44')
print("Join list of strings to create new string: ", "---".join(list1).upper())


dict1 = {'a':'123', 'b':"one", 'c':{"color":'red',"num":"456"}, 'd':True}
print("print Dictionary", dict1)
print(dict1.keys())
print("values: ", dict1.values())
print(dict1['b'])
dict1['d']=False
print(dict1.get('d'))
