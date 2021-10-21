'''#PYTHON FILE HANDLING
#Python provides the facility of working on Files. A File is an external storage on hard disk from where data can be stored and retrieved.
#HERE WE CAN CREATE NEW FILE IN ANY FORMAT SUCH AS .TXT,.DOC., .XLS,.CSV,.PPT
# THIS WILL INTAKE ONLY STRING VALUES. LIST and TUPLE to be converted to STRING, then only they will be stored.

#Syntax to generate new file is :-  obj=open(filename , mode). 
#DIFFERENT MODES ARE:- 
# R:- It opens in Reading mode. It is default mode of File. Pointer is at beginning of the file.
# W:- Opens file in Writing mode. If file already exists, then overwrite the file else create a new file.
# a:- Opens file in Appending mode. If file already exists, then append the data at the end of existing file, else create a new file.

#Refer below example. Object = f, file name = maheshnewfile.txt", mode = w

f=open ("maheshnewfile.txt","w")  #--> This "OPEN" will generate new .txt file with name 'maheshnewfile.txt' and "w" will allow us to write
f.close() #--> This will close the file

#WRITE SECTION (w)
#NEW TXT FILE NAMED AS "maheshnewfile.txt" is crearted. Let us write into it.

f=open ("maheshnewfile.txt","w") 
f.write("This is a demo file for python handling learning") #--> WRITE' will allow us to write in file. This will be printed in the newly created file. 
f.write ("\n Happy Diwali")
f.write ("\n Hi")
l= ["\n abc", "\n 45", "\n 25.65"] #--> Here List is converted to strings by keeping them in QUOTES
f.writelines(l)  #--> This will allow us to write various lines i.e. list or tuple
f.close()

#NEW DOC FILE NAMED AS "maheshnewfile.txt" is crearted
f=open ("maheshnewfile.doc","w") 
f.write("This is a demo file for python handling learning")
f.close()

#NEW PPT FILE NAMED AS "maheshnewfile.txt" is crearted
f=open ("maheshnewfile.ppt","w") 
f.write("This is a demo file for python handling learning")
f.close()

#READ SECTION (r)
f=open ("maheshnewfile.txt","w") #--> File generate karke ussmein likha
f.write("This is a demo file for python handling learning") #--> WRITE' will allow us to write in file. This will be printed in the newly created file. 
f.write ("\n Happy Diwali")
f.write ("\n Hi")
l= ["\n abc", "\n 45", "\n 25.65"]
f.writelines(l) 
f.close()
#Above section ko humne pehle ek file jiska naam hai "maheshnewfile.txt" usmein likha...Ab hum usse read karenge

f=open ("maheshnewfile.txt","r") 
data=f.read(22)  #--> This will READ ONLY FIRST 22 CHARACTERS including spaces and gaps
print(data)

f=open ("maheshnewfile.txt","r") 
data=f.readline()  #--> This will read ONLY FIRST COMPLETE LINE including spaces and gaps
print(data)

f=open ("maheshnewfile.txt","r") 
data=f.readlines()  #--> This will read ALL COMPLETE LINES including spaces and gaps
print(data)


print("Name of file:-", f.name)   #--> This will tell what is the name of file. O/P is:- maheshnewfile.txt
print("Mode of file:-", f.mode)  #--> This will tell what is mode of file Read(r), Write(w) or Append(a). O/P is:- r
print("File is readable or not:-", f.readable()) #--> This will tell whether file is readable or not (If readable-True, If not readable-False).  O/P is:- True
print("File is closed or not:-", f.closed) #--> This will tell file is closed or not(If closed-true, if not closed-false). O/P is:- False.. Means file is still open
f.close()    #--> Now we have closed the file. lets check whats it status now 
print("Now Closed or not:-", f.closed)  #-->This will tell file is closed or not(If closed-true, if not closed-false). O/P is:- True. Means file is closed now

#APPEND SECTION (a)
f=open("appendfile.txt", "a") #--> This will open a txt file named "appendfile.txt" and will permit us to append..yani aage aage add karte jaana..it will not replace previous entered data
for i in range (1,4):   #-->for loop chaliye 3 times ke liye..mentioned minus 1 hota hai na for loop mein
    no = input("Enter number:-") 
    name = input("Enter name:-")
    f.writelines([no,"\t", name,"\n"])  #--> Variables ka data jo hum enter karenge woh puri Lines print karwayi 

f.close()

#JITNI BAAR ABOVE CODE RUN KAROGE UTNI BAAR NEW DATA "appendfile.txt" MEIN ADD HOTA JAYEGA.

# AGAR HUM TYPE KARE:- 
# w+ --> WRITE PLUS READ
# r+ --> READ PLUS WRITE
# a+ --> READ, WRITE PLUS APPEND

f= open("student.txt", "w+")  #--> This will help to read and write
f.writelines (["No \tNames \tMarks1 \tMarks2 \ttotal \n"])  #--> Print the TITLES
while True:
    No = input("Enter student roll no:-")
    Name= input("Enter student Name:-")
    Marks1 = input ("Enter student Marks1:-")
    Marks2 = input ("Enter student Marks2:-")
    total = int(Marks1) + int(Marks2)
    f.writelines([No,"\t", Name, "\t", Marks1, "\t", Marks2, "\t", str(total), "\n"]) #--> Yaha total str mein likhna padega warna add nahi karega..int likha toh error dega kyunki int woh pehchanta nahi
    choice = input("Add more data (Y/N):-")
    if choice.upper()== "N":  #--> Agar humne Y ya N small letters mein bhi dala toh bhi yeh usse UPPER case mein kardega 
        break
    
print ("Tell the location of pointer:-", f.tell())  #--> f.tell() POINTER KI CURRENT POSITION BATATA HAI
f.seek(0)   #--> Yeh pointer ko bracket mein likhi hui position tak lejata hai.
data=f.read()  #--> Yaha pointer ZERO pe aya hua hai..isliye starting se read karega aur pura code data naam ke variable mein store kardega aur fir hum print karsakte hai
print (data) 

f.close()'''


#CSV FILE HANDLING
import csv

heading=["Name","Age","Marks"]

'''data=[['abc',56,78.96],['xyz',20,78.7],['mno',56,82],['dws',32,74]]

with open('testcsv.csv','w',newline='') as f:
    cw=csv.writer(f,delimiter=',')  
    cw.writerow(heading)
    cw.writerows(data)
    for i in data:
        cw.writerow(i)

    f.close()'''

'''l1=[]
data=[]
with open('testcsv123.csv','w',newline='') as f:
    cw=csv.writer(f,delimiter=',')
    cw.writerow(heading)
    for i in range(1,4):
        name=input("Enter name:- ")
        age=int(input("Enter age:- "))
        marks=float(input("Enter marks :- "))
        data=[name,age,marks]
        print("data:- ",data)
        l1.append(list(data))
        print("l1:- ",l1)
        
    cw.writerows(l1)
    f.close()'''

with open('testcsv.csv','r',newline='') as f:
    cr=csv.reader(f)
    for d in cr:
        for i in d:
            print(i,end=" ")
        print()
        
