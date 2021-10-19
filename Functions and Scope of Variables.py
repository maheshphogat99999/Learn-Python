'''#FUNCTIONS
# SYNTAX OF FUNCTION:- def functionname (parameters):
# SYNTAX OF FUNCTION CALLING:- fucntionname (parameters)

#1. EXAMPLE

def func1(n1,n2):     #--> FUNCTION DEFINITION
    print("Value of n1:-",n1)
    print ("Value of n2:-",n2)
    
func1(20.2, 30)     #--> FUNCTION CALLING

#IN ABOVE CODE 20.2 will be assigned to n1 and 30 will be assigned to n2

#2. EXAMPLE
def func(n1,n2=2): #--> Here compulsory value of n2 will be taken as 2
    print("N1:-",n1)
    print("N2:-",n2)

func(10)  #--> No need to define n2 as we have put its compulsory value. If we assign new value here then it will overwrite the compulsory value

#3. EXAMPLE
def func(n1,n2):
    print("N1:-",n1)
    print("N2:-",n2)

func(n2=30, n1=10) #--> Koi fark nahi padta, you can also write n2 before n1 as we have particularly defined it



#4. EXAMPLE
a= int(input("Enter the value of N1:-"))
b= int(input("Enter the value of N2:-"))

def func1(a,b):
    print ("Function Operation:-", a+b)

func1(a,b)

#5. RETURN EXAMPLE

def func2(n1,n2=20):   
    return n1-n2    #--> Return ke baad expression dena hi padega, kyunki kya return karvana hai wohi batega

print("Answer is:-", func2(100)) #--> n2 ki value yaha mention nahi ki hai, kyunki woh predefined, compulsory dedi hai'''

'''

#LAMBDA / ANONYMOUS FUNCTION
mul=lambda n1,n2:n1*n2  #--> Mention variable name: Mention operation to be performed
print ("Multiplication:-", mul(5,7))   #--> Enter values of variables. Yaha int(input pehle bhi karva sakte hai.

n1=int(input("Enter the value of N1:-"))
n2=int(input("Enter the value of N2:-"))
m=lambda n1,n2:n1 if(n1>n2) else n2  #--> Pehle jo answer chaiye (n1) woh ayega, fir condition or fir else agar condition satisfy na ho toh
print(m(n1,n2))


n1=int(input("Enter the value of N1:-"))
n2=int(input("Enter the value of N2:-"))
m=lambda n1,n2:n1 if(n1>n2) else True if (n1==n2) else n2
if (m(n1,n2)==True):   #--> m ka n1 aur n2 agar equal hai..toh true hoga aur agar true hoga..tabhi next line print hoga..warna else pe jump kar jayega
    print ("Both numbers are same")
else:
    print(m(n1,n2),"is maximum")


#SCOPE OF VARIABLE
#There are two types of variables based on Scope: 1) Local Variable. (JO SIRF def ke andar accesssible hai woh) (2) Global Variable. (Jo def ke bahar aur andar dono jagah accessible hai)
#1) LOCAL VARIABLE :- Variables declared inside a function body is known as Local Variable.
#These have a local access thus these variables cannot be accessed outside the function body in which they are declared.

#2) GLOBAL VARIABLE:- Variable defined outside the function is called Global Variable. Global variable is accessed all over program

a=10 #--> GLOBAL VARIABLE
def demo():
    b=20   #--> LOCAL VARIABLE
    print(b)
demo()

#Yaha in above code only LOCAL is getting printed, GLOBAL IS NOT GETTING PRINTED.. AGAR GLOBAL KO BHI ANDAR LENA HAI TOH...
a=10 
def demo():
    global a #--> agar global na likha toh error ayega, kyunki a ko woh define hi nahi kar payega
    b=20
    b=b+10
    a=a+10
    print("Value of b:-",b)
    print("Value of a:-",a)

a=a+10 #--> Yaha 20 ki value milegi aur fir usmein 10 add kar dega toh 30 ho jayegi total
demo()


#ASSIGNMENT-10
#Q1.  Create one function Rectangle. and calculate area of  them using function. Area of a Rectangle = Base × Height.

base=int(input("Enter the value of Rectangle Base:-"))
height=int(input("Enter the value of Rectangle Height:-"))

def Rectangle(base, height):
    print("The area of rectangle is :-", base*height)

Rectangle(base,height)

#Q2. Create one function square and calculate  area  of them using function. Area of a Square = s2

sq=int(input("Enter the value to be squared:-"))

def square(sq): #--> As Only one variable is unknown thats why not inserting second variable
    print(" The squared value is:-", sq**2)

square(sq)

#Q3. Create one function circle and calculate area of  them using function. Area of Circle = π(radius)2 = πr2

import math 
math.pi
pi=math.pi 

#Above is the way to import predefined value of pi. If we dont want this then we can directly type 3.14 in the equation

rad= int(input("Enter the value for Circle radius:-"))
pi=math.pi
def circle(rad):   #--> As Only one variable is unknown thats why not inserting second variable
    print("The area of circle is:-", pi*(rad**2))

circle(rad)


#Q4. Create one function cube and calculate area of them using function. Area of Cube (surface)	= 6 × side2

sd= int(input("Enter the value for Circle radius:-"))
def cube(sd):
    print("The surface area of cune is:-", 6*(sd**2))

cube(sd)

#Q5. Create Menu: - Function should be 1. Rectangle 2. Square 3. Circle 4. Cube. Display all function and perform all operation. Calculate them. (use if else to perform).

print("Enter  1 for Rectangle","\n" , "Enter 2 for Square","\n", "Enter 3 for Circle","\n", "Enter 4 for cube")
choice=int(input("Enter your value for required operation:-"))
if (choice==1):
    base=int(input("Enter the value of Rectangle Base:-"))
    height=int(input("Enter the value of Rectangle Height:-"))
    def Rectangle(base, height):
        print("The area of rectangle is :-", base*height)

    Rectangle(base,height)

elif(choice==2):
    sq=int(input("Enter the value to be squared:-"))
    def square(sq): #--> As Only one variable is unknown thats why not inserting second variable
        print(" The squared value is:-", sq**2)

    square(sq)

elif(choice==3):
    import math 
    math.pi
    pi=math.pi 
    rad= int(input("Enter the value for Circle radius:-"))
    pi=math.pi
    def circle(rad):   #--> As Only one variable is unknown thats why not inserting second variable
      print("The area of circle is:-", pi*(rad**2))

    circle(rad)
    
elif(choice==4):
    sd= int(input("Enter the value for Circle radius:-"))
    def cube(sd):
       print("The surface area of cune is:-", 6*(sd**2))

    cube(sd)

else:
    print("Entered Choice Is Wrong, Please Select Correct Choice")

#Q6. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


x= int(input("Enter the value for which factorial is to be calculated:-"))
def facto(x):
    if(x<0):
      print ("Negative Number cannot have factorial")
    else:
     if (x==0):
      f=1
     else:
      f=1
     for i in range (1,x+1):
       f=i*f
     print ("Factorial is",f)

facto(x)

#Q7. Write a Python function that takes a number as a parameter and check the number is prime or not
#Note: A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself. 

def prime(z):
    flag=0
    if(z>1):
        for i in range (2,z):
            if(z%i==0):
                print(z, "is not a prime number")
                flag=1
                break
        else:
            print(z, "is a prime number")
            

        if(flag==1):
            print(z, "is not a prime number")
           
        else:
            print(z, "is a prime number")
    else:
        print("Kindly enter value greater than zero")
        
z=int(input("Enter numeric value to checking whether it is a prime number or not:-"))
prime(z)

#OR SECOND WAY TO WRITE CODE

def prime(z):
    if(z>1):
        for i in range (2,z):
            if(z%i==0):
                print(z, "is not a prime number")
                break
        else:
            print(z, "is a prime number")  
    else:
        print("Kindly enter value greater than zero")
        
z=int(input("Enter numeric value to checking whether it is a prime number or not:-"))
prime(z)'''

