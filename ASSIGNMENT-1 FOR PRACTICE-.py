# Assignment-1.

# Q1. Relation between Celsius and Fahrenheit is governed by the formula (F = 9C/5 + 32). Write a program to convert the temperature (1) From Celsius to Fahrenheit and (2)From Fahrenheit to Celsius
#Here we will enter value two times for vice-versa conversion
'''c=float(input("Enter the value in Degree Celcius:-"))
f=(((9*c)/5)+32)
print("Degree Celcius to Farenhiet Conversion is",f)
f1=float(input("Enter the value in Farhenheit:- "))
c=(((f-32)*5)/9)
print("Farhenheit to Degree Celcius Conversion is",c)

#Here Degree Celcius value will be added only once for vice-versa conversion, It will convert To farenheit and back to degree celcius
c=float(input("Enter the value in Degree Celcius:-"))
f=(((9*c)/5)+32)
print("Degree Celcius to Farenhiet Conversion is",f)
c=(((f-32)*5)/9)
print("Farhenheit to Degree Celcius Conversion is",c)'''

#Q2.Print student Information. Student number, student name, marks of 4 subjects and display total and average 
a=input("Enter student name:-")
b=input("Enter student enrollment no.:-")
c=float(input("Enter English Marks:-"))
d=float(input("Enter Maths Marks:-"))
e=float(input("Enter Science Marks:-"))
f=float(input("Enter Social Science Marks:-"))
g=(c+d+e+f)    # Summation of all marks will be done
print("Total Marks scored:-",g) # Total Marks will be printed
h=(g/4)     #This formula will convert it into average
print("Average:-",h)  # Average value will be printed

#Q3. Write a Python program for to print cube of given number. [i.e. input=2, output=8 (2*2*2)]
a=float(input("Enter the value:-"))
b=a**3  # ** means raise to
print("Cube:-",b)
        
#Q4. write a Python program to find area of trapezoid area = ½ (a+b) * h, wherea & b are length of parallel side of trapezoid, h-height of trapezoid
a=float(input("Enter the value of side1:-"))
b=float(input("Enter the value of side2:-"))
h=float(input("Enter the value of height:-"))
c=(((0.5*(a+b))*h)) 
print("The total area of trapezoid is:-",c)

#Q5. write a Python program to calculate the volume of spherical cap volume = V = (Pi/6) *(3*r12+h2) *h
a=float(input("Enter the value of r1:-"))
b=float(input("Enter the value of h:-"))
v= ((3.14/6)*(((3*(a**2))+(b**2)))*b)
print("Volume:-",v)
             

#Q6. write a Python program to calculate total surface area of rectangular parallele piped area = 2 (ab + ac + bc)
a=float(input("Enter the value of a:-"))
b=float(input("Enter the value of b:-"))
c=float(input("Enter the value of c:-"))
d= 2*((a*b)+(a*c)+(b*c))
print("Total surface area of rectangular parallel pipe is:-",d)'''
