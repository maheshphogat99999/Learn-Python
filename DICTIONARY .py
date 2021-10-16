#PYTHON DICTIONARY IS SOMEWHAT DIFFERENT THEN LIST AND TUPLE, WHICH IS AS MENTIONED BELOW:-
# "dict" is used to convert into dictionary

data = {'a': 90, 'abc': 20, 15: 'xyz', 56.63: 89, 1: 'x', 2: 85}

# "data" is a name of dictionary. DICTIONARIES ARE REPRESENTED BY CURLY BRACKETS {}. Dictionary is a group of ITEMS. Dictionary DONT HAVE Index Numbers as List or tuple.
#Thus, any value can be stored anywhere

#Each dictionary has individual ITEMS. E.G. :-  'a': 90 is an item
                                              #'abc': 20 is an item

#Each ITEM consists of TWO Parts (1) KEY (2) VALUE. Both these are to be seperated by COLON(:). Refer "data"
E.G. :-  'a' is a KEY  and 90 is VALUE
       #'abc' is a KEY and 20 is VALUE

# EVERY KEY IS UNIQUE. YOU CANT REPEAT KEY.

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
print("Dict:- ",d1)
print("The values of mentioned keys are:- ",d1[15],d1[10])   #--> This will FETCH AND DISPLAY the MULTIPLE values assigned to MULTIPLE KEYS 15 and 10. Thus the answer will be "xyz" and 10


d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
d1['a']= 90
print("Update the value:- ",d1)  #--> This will UPDATE/REPLACE the value of KEY 'a' from 56 to 90

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
d1['a'], d1[15], d1[10]= 90,"m","n"
print("Update the value:- ",d1)  #--> This will UPDATE/REPLACE the MULTIPLE values of KEY 'a' from 56 to 90,  of KEY 15 from xyz to "m" and of KEY 10 from 150 to "n"

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
d1.update({1:"x",2:85})    #--> As KEYS 1 and 2 are not available in dictionary d1, thus, here IT WILL ADD these NEW ITEMS AT THE END  after LAST ITEM 56.63:89 
print("Newly inserted values are:- ",d1)

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
del d1[10]   #---> This will DELETE the value of "KEY 10 and its value 150" and display the dictionary without that item
print("delete:- ",d1)

d1.clear()  #---> This will DELETE THE COMPLETE DICTIONARY
print("Clear:- ",d1)

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
d2={}     #---> This is blank dictionary
d2=d1.copy()    #---> This will COPY dictionary d1 into d2
print("Copied dictionary:- ",d2)    #--> This will display d2, which is now similar to d1

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
print("length of d1 is:- ",len(d1)) #---> This will display TOTAL NUMBER OF ITEMS in dictionary. In d1 there are total 5 items 

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
print("Value of entered key is:- ",d1.get(10)) #---> This will display the VALUE OF ENTERED KEY  

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
print("Keys are:-", d1.keys()) #---> This will identify and DISPLAY ALL THE KEYS of ITEMS LISTED/ASSIGNED IN THE DICTIONARY d1

#2nd METHOD TO IDENTIFY ALL KEYS

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
k=d1.keys()
print("\n keys:- ")
for i in k:
    print(i,end="\t")


d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
print("Values are:-", d1.values()) #--> This will identify and DISPLAY ALL THE "VALUES" of d1. 

#2nd METHOD TO IDENTIFY ALL "VALUES" of all the ITEMS


d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
v=d1.values()
print("\n values:- ")
for i in v:
    print(i, end="\t")

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
print("Items are:-", d1.items())#---> This will display ALL THE ITEMS of dictionary d1.

#2nd METHOD TO IDENTIFY ALL "ITEMS" of all the ITEMS
d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
a=d1.items()
print("\n items:- ")
for i in a:
    print(i,end="\t")


d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}   
d1.pop(15)    #--> This will DELETE the ITEM having key 15 alongwith its value.
print("pop:- ",d1)

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89} 
d1.popitem()  #---> This will DELETE ONLY LAST ITEM
print("Updated list after deleting last item:-",d1)


#ASSIGN SAME VALUES TO ALL KEYS WITH THE HELP OF FROMKEYS.

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}  
print("Replaced values of all keys are:", d1.fromkeys((d1),1000)) #--> This will assign SAME VALUES TO ALL THE KEYS of d1.

#If we wnat to assign same values to only fixed number of keys, that is also possible. But it has to be done in square brackets

d1={10:150,'a':56,"abc":20,15:"xyz",56.63:89}
print("Replaced values of all keys are:",d1.fromkeys(["a", 15, 56.63],9000)) #--> Value of KEYS "a", 15, 56.63 are now changed to 9000

#NESTING OF DICTIONARY

d1={1:"a",2:3, 3:{10:1,20:3,40:5}} #--> Here 3 is the KEY and {10:1,20:3,40:5} are all the VALUES OF 3. Here dictionary ke andar ek aur dictionary hai.
print("Nested dictionary:-", d1[3] [40])  #--> d1 is main dictionary, [3] is the KEY of main dictionary d1, [40] is KEY of Nested dictionary 3. So it will display the value of KEY 40 i.e. 5
