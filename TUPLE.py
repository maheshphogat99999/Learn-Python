# TUPLE IS IMMUTABLE. YOU CAN'T CHANGE THE TUPLE. ONCE CREATED ALL THE INDEXES AND THERE VALUES ARE FIXED.
# ONLY FEW THINGS ARE PERMITTED ON TUPLE BECAUSE YOU CANT CHANGE OBJECT VALUES.
# UPDATING THE TUPLE IS NOT POSSIBLE. DELETING ANY OBJECT FROM TUPLE IS NOT POSSIBLE
# INSERT, REMOVE, DELETE, REVERSE, SORT, REVERSE-SORT, POP IS NOT POSSIBLE BECAUSE THEY CHANGE THE OBJECT INDEXES. 


#1st 
#TUPLE OF TUPLE
t=(100,"abc",56.63,"a", 85,20)
t1=(t,14,23,25)
print(t1)
# Here output of above will be((100, 'abc', 56.63, 'a', 85, 20), 14, 23, 25)
#Kindly see that t is generated within brackets and rest are out of brackets.
#Here in t1...complete t will have index value ZERO (0), 14 will have index 1,23 will have 2

#2nd 
t=(100,"abc",56.63,"a", 85,20)
t1=(14,23,25)
t=t+t1
print(t)
# Output:- (100, 'abc', 56.63, 'a', 85, 20, 14, 23, 25)--> Both are added but t1 is added in last of t. This is similar to what happens in list

#3rd
t=(100,"abc",56.63,"a", 85,20)
print("The object value located on entered index no.:-", t[3])
# OUTPUT:- The object value located on entered index no.:- a

#4TH
t=(100,"abc",56.63,"a", 85,20,100,200,500)
print("The list of all objects located between:-", t[3:7])
#OUTPUT:- The list of all objects located between:- ('a', 85, 20,100) --> It will take upto 6th index no. value

#5th
t=(100,"abc",56.63,"a", 85,20,100,200,500)
print("The list of all objects :-", t[3:])
#OUTPUT: The list of all objects :- ('a', 85, 20, 100, 200, 500)--> Start from 3rd object value till end.

#6th
t=(100,"abc",56.63,"a", 85,20,100,200,500)
print("The list of all objects:-", t[:8])
#OUTPUT:-The list of all objects:- (100, 'abc', 56.63, 'a', 85, 20, 100, 200)-->Start from object having index value 0 till 7th object

#7th
t=(100,"abc",56.63,"a", 85,20,100,200,500)
print("The list of all objects:-", t[::3])
#OUTPUT:- The list of all objects:- (100, 'a', 100)--> Start from object having index value 0 then jump by 2 values and display 3rd value

#8th
t=(100,"abc",56.63,"a", 85,20,100,200,500)
print("The list of all objects:-", t[-3])
#OUTPUT:- The list of all objects:- 100--> It will give you value of object located at -3 position


#9TH. OUTPUTS OF ALL ARE MENTIONED TOGETHER
t=(100,56.63, 85,20,100,200,500)
print ("The minimum value available in tuple t is:-", min(t)) #--> Minimum object value in tuple t
print("The maximum value available in tuple t is:-", max(t)) #--> Maximum object value in tuple t
print("The length of tuple t is:-", len(t))   #---> Total number of objects in tuple t
print("The index value of object:-", t.index(200))  #--> Index value of 200 in tuple t
print("The count of object:-",t.count(100)) #--> Number of times 100 present in tuple t
print("Multiply 2 times:-", 2*t) #--> Tuple t will be printed 2 times

'''#OUTPUTS OF ABOVE CODES
The minimum value available in tuple t is:- 20
The maximum value available in tuple t is:- 500
The length of tuple t is:- 7
The index value of object:- 5
The count of object:- 2
Multiply 2 times:- (100, 56.63, 85, 20, 100, 200, 500, 100, 56.63, 85, 20, 100, 200, 500)'''

