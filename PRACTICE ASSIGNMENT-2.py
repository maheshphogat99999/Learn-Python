#ASSIGNMENT-2,Q1
#Write a Python program to find whether entered number is positive, negative or zero
n= int(input("Enter the value of n:-")) #Only integer value is accepted
if (n>0):                               # First "if" condition
    print(" is a positive  number")  
elif(n==0):                             # Instead of giving every time if-else statements, we can directly write "elif" for the mid conditions. Use this when more then 2 conditions are to be assessed.
    print (" is zero")  
else:
    print("n is negative number")
 
# ASSIGNMENT-2 QUESTION-2 :- FIND ODD OR EVEN
#CHECK THIS .IT WILL GIVE WRONG ANSWER (WRONG CODE)
n= int(input("Enter the value of n:-"))
if (n/2):
    print("n is even number")
else:
    print("n is odd number")

#ABOVE CODE WILL ALWAYS SHOW ALL THE ENTERED NUMBERS AS EVEN NUMBERS. Refer the condition properly, It is mentioned "if(n/2)". No matter whether you enter Even or odd number, all these will be divisble by 2
# Thus, we cant keep this condition of n/2 to identify whether a number is even or odd. So we have to keep if n%2==0
# Division operator = /
# Modulus or Remainder operator = %
# Floor Division or Quotient operator= //

#RIGHT CODE FOR FIND ODD OR EVEN
n= int(input("Enter the value of n:-"))
if (n%2==0):
    print("n is even number")
else:
    print("n is odd number")

#Above code will run right for all values. BUT WHAT IF WE ENTER N=0?

# THUS BELOW ARE THE TWO METHODS OF WRITING DOWN THE CORRECT CODE.
#METHOD-1
n= int(input("Enter the value of n:-"))
if (n%2==0):
    if(n==0):
     print("n is zero")
    else:
     print("n is even number")
else:
    print("n is odd number")

#METHOD-2
n= int(input("Enter the value of n:-"))
if (n==0):
    print("n is zero")
elif (n%2==0):
     print("n is even number")
else:
    print("n is odd number")

#ASSIGNMENT-2 QUESTION-3 (FIND GREATEST AMONG THREE NUMBERS)

#METHOD-1
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


#METHOD-2
a= float(input("Enter the value of a:-"))
b= float(input("Enter the value of b:-"))
c= float(input("Enter the value of c:-"))
if(a>b and a>c):
    print(a, "a is maximum value")
elif(b>a and b>c):
    print(b, "b is maximum value")
    
elif(a==b==c):
    print("All values are equal")
else:
    print(c,"c is maximum value")

# IN ABOVE MENTIONED BOTH THE METHODS, CODE IS NOT OK. IT IS INCORRECT, REASON FOR THE SAME AS MENTIONED BELOW
#If we enter
#Enter the value of a:- 3
#Enter the value of b:- 2
#Enter the value of c:- 3
#O/P= 3.0 c is maximum value

#Actually 3 is assigned to "a" as well as to "c", but in the output results are shown only for "c".


#Thus below mentioned code is to be used for such kind of problems.

a= float(input("Enter the value of a:-"))
b= float(input("Enter the value of b:-"))
c= float(input("Enter the value of c:-"))
if(a>b and a>c):
 print(a, "a is maximum value")
elif(b>a and b>c):
    print(b, "b is maximum value")
elif(c>a and c>b):
    print(c, "c is maximum value")
else:
    if(a==b==c):
        print("All values are equal")
    elif(a==b and a>c):
        print(a, "Both a and b is maximum value")
    elif(b==c and b>a):
        print(b, "Both b and c is maximum value")
    else:
        print(c, "Both a and c is maximum value")
  

#ASSIGNMENT-2,Q4

# Write a Python program that will compute rebate and print an output comprising of three things - Customer Identification number, Purchase Amount and Rebate for each recode.
# The customer identification number is provided to you along with the Purchase amount and the slabs of Rebate. Use the table listed below:

# Amounts of Purchase               Rebates application on purchase amount                                                           			                                             
# =<Rs. 5000				3%
# >Rs. 5000 but <=Rs.10000		9%
# >Rs. 10000				12%

cin=int(input("Enter Customer Identification Number:-"))
pur=int(input("Enter total purchase amount:-"))
if (pur<=5000):
    reb=(pur*0.03)
elif(pur>5000 and pur<=10000):
    reb=(pur*0.09)
else:
    reb=(pur*0.12)
print("Rebate applied is:-",reb)
print("Final amount is:-", pur-reb)


#ASSIGNMENT-3,Q5
# A bookshop sells three types of books, namely science subjects, Commerce subjects and Arts subjects. They offer discount @ 2%, 3% and 4% on respective subjects.
# Besides this the shop also offers another discount @ 2.5% on Gross Amount of purchase, if it exceeds Rs. 200.00. Develop a program to calculate the bill amount for the same.
sci=int(input("Enter amount of Science books:-"))
com=int(input("Enter amount of commerce books:-"))
art=int(input("Enter amount of arts books:-"))
scireb=(sci*0.02)
comreb=(com*0.03)
artreb=(art*0.04)
tamt=(sci+com+art)
reba=(scireb+comreb+artreb)
total=(tamt-reba)
if(total<200):
    print("Final amount:-",total) 
else:
   rebatot=(total*0.025)
   Famt=(total-rebatot)
   print("Total amount is:-",Famt)
   print("Rebate given:-",rebatot)

#In above mentioned code:- If anybody purchases only science books or only commerce books, then everytime, we have to enter other books as ZERO(0).
#It should not be like that. We should enter only data for books which we have purchased and not for every category of books.
#Thus below mentioned code first categorize those sections and then minus discounted prices. So new code as below:-

ans="y"
pr=0
d=0
while(ans=="y"):                                        #---> While loop starts
    print("Type 1 for Science Books")
    print("Type 2 for Commerce Books")
    print("Type 3 for Arts Books")
    choice=int(input("Enter your choice:-"))
    if(choice==1):
        price=int(input("Enter Science books price:-"))
        pr+=price
        di=pr*0.02
        d+=di
    elif(choice==2):
        price=int(input("Enter Commerce books price:-"))
        pr+=price
        di=pr*0.03
        d+=di
    elif(choice==3):
        price=int(input("Enter Arts books price:-"))
        pr+=price
        di=pr*0.04
        d+=di
    ans=input("Do you want to continue (y/n):-")       #----> While loop ends
print("Total price:-", pr)
GA=pr-d
print("GA:-", GA)
if(GA>200):
    FA=GA-(GA*0.025)
    print("FA:-",FA)
else:
    print("FA:-",GA)
                 

