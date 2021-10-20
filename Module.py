'''#MODULE
#MODULE CREATION MEANS, creating a python file, a kind of LIBRARY which helps to create ans store our own program codes and can call them in another file.
#Agar humne koi ek program ka code kiya hai..aur uss pure code ko ya uske kissi varaible ko dusri file mein use karna hai bar bar..toh usse call karna padega aur hum usse use kar sakenge
#For eg. pi ki value agar chaiye,,ya factorial calculate karna hai..toh woh already math ki module file mein hai...
#agar humko pi ki value call karni hai..kissi program mein, ya kissi equation mein toh hum pehle math ka module chalu karte hai aur usmein se pi ki value ko call karte hai.
#for eg..agar humko pi ki value math ki library/module se leni hai toh:-

import math   #--> MATH KA MODULE/LIBRARY KO CALL KIYA...IMPORT ka matlab call karo..but kaha..toh math module ko...isliye module ka name achi tarh se dena hai aur usse yaad rakhna hai 
math.pi      #--> USS MATH KE MODULE KE ANDAR SE pi KI VALUE KO CALL KIYA
ourpi=math.pi   # --> pi ki value jo ayi math library ke andar se usko apni file ki pi (ourpi) mein store kiya aur next line mein print karwa diya
print ("Value of pi is:-",ourpi)  #OUTPUT WILL BE --> Value of pi is:- 3.141592653589793

import math
math.sin
d=math.sin
x=d(2)
print(x)


import sys
print(sys.builtin_module_names) #--> System ki files ko import karwaya
'''
import math
print (dir(math)) #--> This will tell ki math library mein kauu-kaunse functions hai.
#NOT TO WORRIED ABOUT FUNCTIONS WITH UNDERSCORE(_). Use only Quoted, without underscore

