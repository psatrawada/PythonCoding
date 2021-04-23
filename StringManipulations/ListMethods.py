# list inbuilt methods in python

input = [32,5,"aa", 32,'f',32,66]
print(input)
input.append("one")  # appends at the end
print(input)
input.insert(2,"two") # insert at the index 2
print (input)
input.remove(32)  # removes first matching element
print (input)
print(input.count(32)) # counts number of times the element appeared in list


list2 = [3,5,1,0]
list2.sort()
print (list2)
list2.reverse()
print (list2)
list2.extend(input) # add the input elements to list2 at the end of list
print(list2)
