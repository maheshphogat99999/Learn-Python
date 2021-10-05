# LOGICAL OPEARTORS = AND,OR,NOT

# (1) EXAMPLE OF "AND" LOGICAL OPERATOR (IF All CONDITIONS are supposed to be SATISFIED/TRUE, then and only then it will show true) 

n1=int(input("Enter n1:-"))    # This will allow user to Enter the interger value and assign that value to variable "n1" 
n2=int(input("Enter n2:-"))    # This will allow user to Enter the interger value and assign that value to variable "n2"
print("Answer is:-", n1==10 and n2==20)   #Here we have assigned a fixed value to n1 and n2.
#If a user enters value of n1=10 and n2=20, then it will display us TRUE because both conditions are TRUE

#OUTPUT WILL BE LIKE THIS
#Enter n1:-10
#Enter n2:-20
#Answer is:- True

#Now if we write: print("Answer is:-", n1==10 and n2==30)  #Here we have assigned a fixed value to n1=10 and n2=30.
#Now if user enters n1:-10 and n2:-20 THEN Answer is:- False (Beacuse one of the value i.e. n2 is not matching. IT IS FALSE VALUE)


# (2) EXAMPLE OF "OR" LOGICAL OPERATOR (It will show true , if ANY ONE CONDITION IS SATISFIED/TRUE, no matter if all other are conditions are false/not satisfied )
n1=int(input("Enter n1:-"))
n2=int(input("Enter n2:-"))
print("Answer is:-", n1==10 or n2==20)

#OUTPUT OF ABOVE CODE WITH DIFFERENT CONDITIONS
#Display will show the answer as below, 
#Enter n1:-10  
#Enter n2:-20
#Answer is:- True     #Because both conditions are matching, as assigned in the code

#Now if we write: print("Answer is:-", n1==10 or n2==30)
#And enter the same values again
#Enter n1:-10
#Enter n2:-20
#Answer is:- True (Beacuse ONE of the value is matching i.e., n1=10)

#Now if we write: print("Answer is:-", n1==10 or n2==30) 
# OUTPUT
#Enter n1:-50     
#Enter n2:-60
#Answer is:- False (Because none of the value is matching,BOTH ENTERED VALUE OF n1 and n2 ARE WRONG)


# (3) EXAMPLE OF "NOT" LOGICAL OPERATOR (This will REVERSE the answer i.e. If the ACTUAL answer is TRUE, then it will show us FALSE. This is just to cross-check. Not generally used) 
n1=int(input("Enter n1:-"))
n2=int(input("Enter n2:-"))
print("Answer is:-", not(n1==10 and n2==20))

#OUTPUT
#Enter n1:-10
#Enter n2:-20
#Answer is:- False (Because actual answers are true, both values are matching, but as we have used "not" it has reversed the answer, thus it is showing False)



# (4) EXAMPLE OF MEMBERSHIP PYTHON OPERATORS ("in", "not in")
# THESE OPERATORS TEST WHETHER A VALUE IN SEQUENCE IS A MEMBER OF SEQUENCE OR NOT. SEQUENCE CAN BE WRITTEN IN LIST, STRING OR TUPLE FORMATS

#LIST - Displayed in square brackets [ ]. This can include, numbers and alphabets both. But alphabets are to be written in quotes. Separate each by comma.
#eg of list:- l=[10, 20,"abc", "bdq", 20.56, 90.36]

#STRING - Displayed in quotes " ". This can include, numbers and alphabets both all in quotes, seperated by commas
#eg of string:- s= "abc", "bdq", "2", "20.34"

#TUPLE - Displayed in parenthesis ( ). This can include, numbers and alphabets both, separated by commas
#eg of string:- s= ("abc", "bdq",2,20.34)

#EXAMPLE OF "in" OPERATOR
#l=[10, 20,"abc", "bdq", 20.56, 90.36]--->(This is list, see bracket shape). Same can be done for string and tuple.
print ("This is your answer:-", 10 in l)
#Above will be displayed as:-
# This is your answer:- True (Because 10 is available in our variable "l")

print ("This is your answer:-", 100 in l)
#Above will be displayed as:-
# This is your answer:- False (Because 100 is not available in our variable "l")

s="abc","20.34", "20", "3td" #--->(This is string)
print ("This is your answer:-", "3td" in s)
# Above will be displayed as :- This is your answer:- True (Because "3td" is available in our variable "s")


t = (10, 20,"abc", "bdq", 20.56, 90.36)
print ("This is your answer:-", 20.56 in t)
#Above will be displayed as :- This is your answer:- True (Because 20.56 is available in our varaible "t")

#Now if we write below code:- 
print ("This is your answer:-", 20.57 in t)
#Above will be displayed as :- This is your answer:- False (Because 20.57 is not available in our sequence, it has to match exactly). This happens for all list, strings and tuple.

#Now if we write
#print ("This is your answer:-", "20.56" in t)
#Then the answer will be FALSE. Beacuse in "t" - 20.56 is displayed as float value and in program we have kept it in "QUOTES" so the python will understand it as STRING value and not float value. So it will show false.


#EXAMPLE OF " not in" OPERATOR. (If the value is there it will show False in result, and if the value is not there, then it will show TRUE, because we are using NOT IN- andar nahi hona chaiye)
t=(10, 20,"abc", "bdq", 20.56, 90.36)   #---> same can be done for list and strings
print ("This is your answer:-", 20.56 not in t)
#This is your answer:- False #(Because we have used not in i.e. REVERSE DETECTION/CROSS-CHECKING. If value is there, then it should show FALSE. If value is NOT THERE, it should show TRUE.
# 20.56 is there in the variable "t", and in code we have used "NOT IN" , thus it will show False
