#ASSIGNMENT-4, Q1 (NESTED FOR LOOP)
#START WITH PRINTING STARS OR ANY PARTICULAR DIGIT
#FOR 5x5 matrix
n=int(input("Enter the value:-"))
for row in range (1,n+1): #---> This is main "for" loop. This always runs for ROWS. "row" is a variable name..We can take any other name too. It will take one number less thus n+1 is mentioned.
    for col in range(1,n+1): #----> This is nested for loop. This always runs for COLUMNS. "col" is a variable name, we can take any other variable too.
        print("*", end=" ")  #--->This will allow what to print.  Here star will be printed  
    print()              #-----> This will allow to print in next line

#AS PER ABOVE CODE, BELOW WILL PRINT 5 IN ALL ROWS AND COLUMNS
n=int(input("Enter the value:-"))
for row in range (1,n+1): 
    for col in range(1,n+1): 
        print("5", end=" ") #-----> Every row aur column  "5" will be printed   
    print() 


"row" and "col" ARE JUST NAMES OF VARIABLES. WE CAN SELECT OTHER NAMES TOO. FOR EXAMPLE REFER BELOW CODE:
n=int(input("Enter the value:-"))
for a in range (1,n+1): 
    for b in range(1,n+1): 
        print("5", end=" ")
    print() 

#NOW LETS SAY IF WE WANT TO PRINT BELOW MENTIONED MATRIX
*                 5            
**                55           
***               555          
****              5555         
*****             55555        

n=int(input("Enter the value:-"))
for a in range (1,n+1): 
    for b in range(1,a+1): 
        print("*", end=" ")
    print()

FOR PATTERN
1
12
123
1234
12345

n=int(input("Enter the value:-"))
for row in range (1,n+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print(" ")

FOR PATTERN
1
23
456
78910

a=1
b=2
n=int(input("Enter the value:-"))
for row in range(1,n+1):
    for col in range(1, b):
        print(a, end=" ")
        a+=1
    print(" ")
    b+=1

#PATTERN FOR SPACE IN FRONT
n=int(input("Enter the value:-"))
for row in range(1, n+1):
    for space in range(1,(n-row)+1):
        print(' ', end=" ")
    for col in range(1, row+1):
        print("*", end=" ")
    print()


#WHILE LOOP
i=1 ---> INITIALIZATION
while(i<=100): -----> CONDITION
    print(i, end="\t") ----->STATEMENT
    i+=1 ----> INCREMENT/DECREMENT

In above i =1, then i+=1 will add 1 and store that value in i. So one loop compelete. Now new value of i is 1+1=2. Thus it will again start while loop from 2 and will reach upto 100
    
#WE CAN ALSO FORCEFULLY STOP THE WHILE LOOP, OTHERWISE IT WILL RUN INFINITE LOOPS
i=1
while(True):
    if(i==100):
        break 
    print(i,end="\t")
    i+=1
Here when value of i=99 and after that with i+=1 will provide answer as 100. As soon as 100 will arrive it will break the loop because we have written i==100 and will not carry any further addition.
Thus, 100 will not be printed in the answer.

ASSIGNMENT -4 Q2 (CALCULATE EVEN AND ODD NUMBERS, COUNT THEM AND DISPLAY THEM)

n=int(input("Enter your number:-"))
i=1
e=0
o=0
print("Even numbers")
while (i<=n):
    if(i % 2 == 0):
        print(i, end= "\t")
        e+=1
    i+=1
print("\n Count of even no.:-",e)
i=1
print("\n odd numbers")
while (i<=n):
    if(i % 2 != 0):
        print(i, end= "\t")
        o+=1
    i+=1
print("\n Count of odd no.:-",o)

#THIS BELOW CODE WILL CALCULATE EVEN AND ODD NUMBERS AND ONLY DISPLAY THEM. IT WILL NOT COUNT, AS ABOVE CODE
n=int(input("Enter your number:-"))
i=1
print("Even numbers")
while (i<=n):
    if(i % 2 == 0):
        print(i, end= "\t") 
    i+=1

i=1
print("\n odd numbers")
while (i<=n):
    if(i % 2 != 0):
        print(i, end= "\t")
    i+=1

#ASSIGNMENT-4, Q-3 FIBIONACCI SERIES 0 TO 50 (THIS SHOULD BE DISPLAYED IN ANSWER-0,1,1,2,3,5,8,13,21,34)
#BASICS OF FIBIONACCI SERIES REFER TO BOOK.
#(FIBIONACCI SERIES MEANS ADDITION OF NUMBER WITH PREVIOUS NUMBER)
#BELOW CODE IS NOT FOR FIBIONNACCI SERIES..IT IS JUST TO IDENTIFY NUMBERS FOLLOWING FIBIONACCI PATTERN TILL NO.5
#IF WE REPLACE 5 WITH 50..WHILE LOOP WILL RUN 50 TIMES AND ANSWER WILL BE WRONG..WE WANT FIOBIONANCCI SERIES TILL NUMBER 50.

i=1
a=0
b=1
while(i<=5):
    print(a,"\n")
    c=a+b
    a=b
    b=c
    i+=1

#BELOW MENTIONED CODE WILL RUN FIBIONACCI SERIES TILL 50
i=0
n1=0
n2=1
for i in range(0,50):
    if(n1<=50):
        print(n1, end="\t")
        n3=n1+n2
        n1=n2
        n2=n3   

#EXPLANATION
#FOR FIRST TIME LOOP
#for i in range(0,50):
#    if(n1<=50): ---->Indicate value less than or equals to 50
#        print(n1)----> Everytime value of n1 will be printed. At this stage it is 0. So 0 will be printed.
#        n3=n1+n2 ----> For 1st loop n1=0, n2=1, Thus n3=1
#        n1=n2 ---> For 1st loop, n1=0 & n2=1, but n1=n2 means we have assigned value of n2 to n1. Thus updated value of n1 will be now 1
#        n2=n3---> For 1st loop, n2=1 & n3=1 as calculated, but n2=n3 means we have assigned value of n3 to n2. Thus updated value of n2 will be 1

#FOR SECOND TIME LOOP        
#for i in range(0,50):
#    if(n1<=50):
#        print(n1)----> Everytime value of n1 will be printed. New value of n1 available from previous step is 1 
#        n3=n1+n2 ----> For 2nd loop, data will be taken from 1st step. Thus, n1=1, n2=1 and now updated value of n3 will be 2
#       n1=n2 ---> For 2nd loop, n1=1 & n2=1, but n1=n2 means we have assigned value of n2 to n1. Thus updated value of n1 will be now 1
#        n2=n3---> For 2nd loop, n2=1 & n3=2 as calculated, but n2=n3 means we have assigned value of n3 to n2. Thus updated value of n2 will be 2

#FOR THIRD TIME LOOP 
#for i in range(0,50):
#    if(n1<=50):
#        print(n1)----> Everytime value of n1 will be printed. New value of n1 available from previous step is 1 
#        n3=n1+n2 ----> For 3rd loop, data will be taken from 2nd step. Thus, n1=1, n2=2 and now updated value of n3 will be 3
#       n1=n2 ---> For 3rd loop, n1=1 & n2=2, but n1=n2 means we have assigned value of n2 to n1. Thus updated value of n1 will be now 2
#       n2=n3---> For 3rd loop, n2=1 & n3=3 as calculated, but n2=n3 means we have assigned value of n3 to n2. Thus updated value of n2 will be 3    
    
    
#FOR FOURTH TIME LOOP 
#for i in range(0,50):
#   if(n1<=50):
#       print(n1)----> Everytime value of n1 will be printed. New value of n1 available from previous step is 2 
#       n3=n1+n2 ----> For 4TH loop, data will be taken from 3rd step. Thus, n1=2, n2=3 and now updated value of n3 will be  5
#       n1=n2 ---> For 4th loop, n1=2 & n2=3, but n1=n2 means we have assigned value of n2 to n1. Thus updated value of n1 will be now 3
#       n2=n3---> For 4th loop, n2=1 & n3=5 as calculated, but n2=n3 means we have assigned value of n3 to n2. Thus updated value of n2 will be 5

#FOR FIFTH TIME LOOP 
#for i in range(0,50):
#    if(n1<=50):
#        print(n1)----> Everytime value of n1 will be printed. New value of n1 available from previous step is 3 
#        n3=n1+n2 ----> For 5TH loop, data will be taken from 4TH step. Thus, n1=3, n2=5 and now updated value of n3 will be 8
#        n1=n2 ---> For 5th loop, n1=3 & n2=5, but n1=n2 means we have assigned value of n2 to n1. Thus updated value of n1 will be now 5
#        n2=n3---> For 5th loop, n2=5 & n3=8 as calculated, but n2=n3 means we have assigned value of n3 to n2. Thus updated value of n2 will be 8

#FOR SIXTH TIME LOOP 
#for i in range(0,50):
#    if(n1<=50):
#        print(n1)----> Everytime value of n1 will be printed. New value of n1 available from previous step is 5 
#        n3=n1+n2 ----> For 6TH loop, data will be taken from 5TH step. Thus, n1=5, n2=8 and now updated value of n3 will be 13
#        n1=n2 ---> For 6th loop, n1=5 & n2=8, but n1=n2 means we have assigned value of n2 to n1. Thus updated value of n1 will be now 8
#        n2=n3---> For 6th loop, n2=5 & n3=13 as calculated, but n2=n3 means we have assigned value of n3 to n2. Thus updated value of n2 will be 13

#AND SO ON TILL n1 doesnt cross 50
        


#ASSIGNMENT-4, Q-4. FACTORIAL OF ENTERED NUMBER

i=1
a=1
while(i<=5):
    a=a*i  ---> a is 1, and i is +=1, thus automatically 1 value increment will happen when 2nd time loop will run. 
    i+=1
print(a)

#BELOW MENTIONED CODE IS CALCULATION OF FACTORIAL WITH THE HELP OF MATH FUNCTION
x=int(input("Enter value:-"))  
import math
math.factorial(x)
ans=math.factorial(x)

print (" Your answer is:-", ans)

#ASSIGNMENT-4, Q-5 Write a program to calculate and print the series as shown: +1-2+3-4+5=3, If input numb=5
#Input number is 5, logic is if we print any number, in front of odd number positive sign should be printed  and for even number negative sign should be printed in front of it

a=int(input("Enter your number:-"))
i=1
ans=0
for i in range(1, a+1):
    if(i%2==0):
        print("-", i,end= "\t")
        ans=ans-i
    else:
        print("+", i, end= "\t")
        ans=ans+i
i+=1  
print("=",ans)

