# THIS IS ABOUT ASSIGNING DATA TO VARIABLE AND DATA ENTRY BY USER

n=5                            # Numerical Values are called as INTEGERS (Display name:- "int")
print ("value of n:-",n)       # Here 5 will be assigned to variable "n"
print ("type of n:-",type(n))  # Here variable TYPE will be shown as output i.e Integer or Float or String. As n=5,thus it is an INTEGER

ch="abc"                       # Alphabetical Values are called as STRINGS (Display name:- "str")
print ("value of ch:",ch)
print ("type of ch:-",type(ch))

f=20.19                        # Decimal Values are called as FLOAT (Display name:- "float")
print("value of f:-",f)
print("type of f:-",type(f))

id_no= input("Enter your id_no:-")     # "input" written at the beginning will permit the user to enter the data
name = input("Enter your name:-")
city = input ("Enter name of city:-")
mobile_no = int(input("Enter your mobile_no:-"))    # "int(input" written at the beginning will permit the user to enter the data in INTEGER FORMAT ONLY. 
education = input("Enter your education details:-")  
salary = float(input("Enter your salary:-"))       # "float(input" written at the beginning will permit the user to enter the data in FLOAT/decimal FORMAT. 
print ("id_no",id_no, "\n name",name, "\n city",city, "\n mobile_no", mobile_no, "\n education",education, "\n salary",salary)


x = input("Enter your id_no:-") 
y = input("Enter your name:-")
z = input ("Enter name of city:-")
a = int(input("Enter your mobile_no:-"))
b = input("Enter your education details:-")
c = float(input("Enter your salary:-"))
print ("x",x, "\n y",y, "\n z",z, "\n a", a, "\n b",b, "\n c",c)
