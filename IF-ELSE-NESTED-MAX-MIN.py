# STATEMENTS:- It is a line which will help to check conditions. Statements are of two types:- 1. CONTROL TYPE 2. LOOPING TYPE
# CONTROL TYPE HAS THREE CATEGORIES:- 1. IF  2. ELSE  3. NESTED IF ELSE
# After "IF" and "ELSE", colon (:) is compulsory

# "IF" STATEMENT SYNTAX

n=int(input("Enter the value of n:-"))
if(n>1 and n<50):
    print(n, "This value is between 1 and 50")

# This "if(n>1 and n<50):" can also be written as "if(1<n<50):"
#1<n<50 means the value of n is smaller then 50 and 1 is smaller then value of n or we can say the value of n is smaller then 50 and n is graeter then 1

#Now if the value entered is greater then 50, it will show us nothing. Thus here comes "ELSE"

# "ELSE" STATEMENT SYNTAX

n=int(input("Enter the value of n:-"))
if(n>1 and n<50):
    print(n, "This value is between 1 and 50")
else:
    print(n, " This value is not netween 1 and 50")




#Question:- Write a program for Maximum number among two numbers

n1=int(input("Enter the value of n1:-"))
n2=int(input("Enter the value of n2:-"))
if(n1>n2):
       print(n1, "n1 is maximum")
else:
    print(n2,"n2 is maximum")

#Now if we enter both value similar i.e n1=10 and n2=10. Then it will show us that n2 is maximum value. BUT WHY?
#Reason:- Conditions are always mentioned in "IF" statement. If those conditions are false, then automatically it will jump to "ELSE" statement.
# and in "ELSE" statement we havent provided any condition (we cant provide condition to else statement). Thus it will directly execute what is to be printed under "ELSE" statement.
# Thus, it will show us "n2 is maximum."

#TO OVERCOME THIS PROBLEM WE USE NESTED ELSE IF.(use "else" "if" inside main "if")

# "NESTED ELSE IF " STATEMENT SYNTAX

n1=int(input("Enter the value of n1:-"))
n2=int(input("Enter the value of n2:-"))
if(n1>n2):      #----> This is main/1st  "IF". If here condition is false, then only it will jump to "ELSE" statement.
       print(n1, "n1 is maximum")
else:           # This is main/1st "Else" condition
    if(n1==n2): # ----> This is 2nd "if" condition, which is provided under 1st "else" . If this gets satisfied/true, then it will be printed otherwise, it will jump on to next/2nd "else"
        print("Both numbers are same")
    else:       #---> (This is 2nd ""else" condition. It will jump here, if 2nd "IF" condition under Main 1st "else" is not satisfied)
        print(n2,"n2 is maximum")


#PRACTICE NESTED ELSE IF Question:- Write a program for Minimum number among two numbers. Take float values
a= float(input("Enter the value of a:-"))
b= float(input("Enter the value of b:-"))
if (a<b):
    print(a,"Value of a is minimum")
else:
    if(a==b):
        print("Value of a and b are same")
    else:
        print(b, "Value of b is minimum")


#PRACTICE Question:- Write a program for Maximum number among three numbers. Take float values (MORE COMPLEX NESTED ELSE IF LOOP)

a= float(input("Enter the value of a:-"))
b= float(input("Enter the value of b:-"))
c= float(input("Enter the value of c:-"))
if(a>b and a>c):
    print(a, "a is maximum value")
else:
    if(b>a and b>c):
      print(b, "b is maximum value")
    else:
        if(a==b==c):
            print("All values are equal")
        else:
            print(c,"c is maximum value")

      
#PRACTICE Question:- Write a program for Minimum number among three numbers. Take float values. THIS HAS ONLY LIMITED USE. 
a= float(input("Enter the value of a:-"))
b= float(input("Enter the value of b:-"))
c= float(input("Enter the value of c:-"))
if(a<b and a<c):
    print(a, "a is minimum value")
else:
    if(b<a and b<c):
      print(b, "b is minimum value")
    else:
        if(a==b==c):
            print("All values are equal")
        else:
            print(c,"c is minimum value")



# MAXIMUM/MINIMUM NUMBER OUT OF THE TUPLE

n=(2.9,3.5,4.0,-5,100.1,6,-7,-9.2,8.9,-50.9)
a = max(n)
print("The largest number is:",a)

b = min(n)
print("The smallest number is:",b) 



