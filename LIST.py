'''#All lists [] are mutable i.e. modifiable
#All contents of list are called as OBJECTS
# All objects have their individual INDEX locations called as "INDEX". In below list 120 has 0 index location, "abc" has 1, 56.63 has 2 and so on...
#      0     1      2      3   4   5  ---> INDEX VALUES. Index location starts from 0
#Z = [120, "abc", 56.63, "a", 56, 30]
#     -6    -5     -4    -3   -2  -1--->REVERSE INDEX VALUES. Reverse index location starts from -1
#There is reverse indexing also available where last value is assigned "-1" value. In list Z,30 has -1 index, 56 has -2, and 120 has -6.

Z=[120, "abc", 56.63, "a", 56, 30,45,78,90]
Y = [1,3,4,6,8,9,12.5]

print("LIST:-", Z,Y)
print("TYPE OF LIST:-", type(Z))
print("TYPE OF LIST:-", type(Y))

Z=Z+Y
print(" Merge List or List Addition:-",Z)
#Above addition doesnt add values of list, but it simply merges two list. So now Z= [120, "abc", 56.63, "a", 56, 30,45,78,90,1,3,4,6,8,9,12.5]


print("The value index number is:",Z[3])
#Above line will select and print 3rd indexed value of the list Z i.e.'a'

print("The values of selected indexed number range is :-",Z[2:7])
#Above line will select and print 2nd to 7th indexed value of the list Z i.e. 56.63,a,56,30,45. Remember it will select one value less i.e upto 45 and not 78

print("The values of this range is:-", Z[1:])
#Above line will select and print all values positioned from index number 1 till end. Remember here it will not print "120" because it has index location 0.

print("The values of this range is:-", Z[:8])
#Above line will select and print all values positioned from index number 0 till index no 7. Remember here it will not print 90 because it has index location 8.
#As mentioned above it will always select one value less. Thus list will start from 120 and end on 78

print ("The values after Jumping the numbers:-", Z[::3])
#Above line will select and print after JUMP of two values (one less then mentioned). So 120, then jump by two values and next value is "a", next is 45.

print ("The values after Jumping the numbers:-", Z[::-3])
##Above line will select and print after JUMP of two values (one less then mentioned). So first value is 12.5, as it is has index value of -1, then jump by two values and next value is 6,
#next is 1.

Z[4:7]=[1000,2000,3000]
print("Updating the list:-", Z)
#Above lines will update 4th,5th and 6th index value numbers by new numbers. Thus 56 will be replaced by 1000, 30 will be replaced by 2000 and 45 will be replaced by 3000

#BELOW CODE SHOWS HOW TO IDENTIFY INDEX NO. OF GIVEN OBJECTS OF THE LIST
for i in range(0,len(Z)):
    print(i, " IS INDEX VALUE OF", Z[i])

#BELOW CODE SHOWS IDENTIFYING REVERSE INDEX VALUES OF THE GIVEN OBJECTS OF THE LIST
for i in range(-1, -(len(Z)+1),-1):
 print(i, "IS INDEX VALUE OF", Z[i])

#BELOW code will append i.e. add object "xyz" in the list but at last position.
Z.append("xyz")
print("Updated list:-",Z)

# Similarly if we want to append more than one objects then run for-loop for the same as mentioned below:-
for i in ["xyz", 20, 3000]:
    Z.append(i)
    print("Updated list is:-", Z)



del Z[2]  #-----> THIS IS INDEXED VALUE OF AN OBJECT "56.63" AVAILABLE IN THE LIST Z.Thus it will delete 56.63
print("Updated list is:-", Z)


del Z[2:7]  #--->This will delete object values which are located at index numbers 2,3,4,5 and 6 i.e. 56.63,a,56,30 and 45
print("Updated list is:-", Z)

del Z[1:] #--->This will delete all object values or complete list except 120 because 120 has index value of 0. And here we have started from 1.
print("Updated list is:-", Z)

del Z[:8] #--->This will delete all object values starting from 120 till object positioned on 7th value i.e. one value less then mentioned. Thus only 90 will be displayed.
print("Updated list is:-", Z)

Z= [120, 'abc', 56.63, 'a', 56, 30, 45, 78, 90, 1, 3, 4, 6, 8, 9, 12.5]
del Z[::3] #--->This line will select, delete and print after JUMP of two values (one less then mentioned). 120 deleted, leave 2 , then deleted "a", then leave other two, "45" deleted
print("Updated list is:-", Z)


Z= [120, 'abc', 56.63, 'a', 56, 30, 45, 78, 90, 1, 3, 4, 6, 8, 9, 12.5]
del Z[::-3]# --> 12.5 deleted, jump of two, 6 deleted, again jump of two 1 deleted, again jump of two 45 deleted
print("Updated list is:-", Z)
'''
Z=[120, "abc", 56.63, "a", 56, 30,45,78,90] 
Y = [1,3,4,6,8,9,12.5]

print("Minimum value from list is:-", min(Y)) #--> This will provide MINIMUM value of the object available in the list. STRING/ALPHABETS should not be there, otherwise it will show error.

print("Maximum value from the list is:-", max(Y)) #--> This will provide MAXIMUM value of the object available in the list. STRING/ALPHABETS should not be there, otherwise it will show error.

print("Length of the list is:-", len(Y)) #--->This will provide total/final number of objects available in the list. Here they are total 7 objects in the list Y.

print("Index location of the particular object:-", Y.index(12.5)) #--> This will show the position number i.e. index number of 12.5. It is located on 6th position.

print("Count of object:-", Y.count(12.5)) #--> This will count how many times a particular object is present. 12.5 is present only one time, thus it will show 1. It will show 0 if we entered some number which is not available in the list.

Y.insert(2, 2000)
print("Inserted value:-", Y) #--> This will insert 2000 on the index value no.2 i.e. between 3 and 4. 2 is INDEX POSITION and 2000 is OBJECT VALUE TO BE INSERTED.

Y.remove(12.5)
print("Remove value from list:-",Y) #--> This will remove 12.5 from the list Z

Y.reverse()
print("Reverse order of the list is:-",Y)#---> This will reverse the order of complete list.

Y.sort()
print("Ascending order of the list is:-", Y)#---> This will arrange and print all objects of the list in ASCENDING ORDER.

Y.sort(reverse=True)
print("Descending order of the list is:-", Y)#---> This will arrange and print all objects of the list in DESCENDING ORDER.

print("Adding up list three times is:-",3*Y)#--> It will NOT MULTIPLY all objects with 3 BUT This will print list 3 times in CONTINOUS fashion

Y.pop()
print("List without last object is:-",Y) #--> This will directly delete THE LAST VALUE/OBJECT OF THE LIST

Y.pop(3)
print("The deleted object of having third index number is:-", Y) #--> This will delete the OBJECT POSITIONED AT INDEX VALUE OF 3.


#RUNLIST. BELOW MENTIONED CODE WILL HELP TO GENERATE NEW LIST. FOR THAT PROVIDE NEW VARIABLE Y but it should be blank and should have type list which is indicated by square brackets[]

Y=[]
for i in range (1,4): # THIS WILL ASK US TO ENTER 3 TIMES(One less then the mentioned 4)
    no= int(input("Enter value:-"))
    name=input("Enter name:-")
    Y.append(no)
    Y.append(name)
    print("Newly updated list is:-", Y)


