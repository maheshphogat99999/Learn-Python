'''#STRINGS
#Strings are mutable i.e. they can be changed. THEY ARE AVAILABLE WITH INDEX VALUES.
# SPACE/GAP IS ALSO ASSIGNED WITH INDEX VALUE. In below mentioned stirng "s", "W" has index number 6 and not 5, because there is gap/space between "O" of Hello and "W" of World. Thus that space is assigned index value 5

s= "Hello World this is python"
print("String:- ",s)


print("The value of mentioned Index number is :- ",s[2]) #--> This will FETCH THE VALUE LOCATED ON INDEX 2 i.e. l (H=0, e=1, l=2, l=3, o=4)

print("The value of mentioned reverese index number is:- ",s[-2]) #--> This will FETCH THE VALUE LOCATED ON REVERSE INDEX -2 i.e. O (n=-1, o=-2, h=-3, t=-4, y=-5, p=-6)

print("The value of mentioned range is:- ",s[1:4]) #--> This will fetch the VALUE OF INDEX NUMBERS FROM 1 TILL 3 (One less than mentioned). i.e ell

print("The value is:- ",s[2:]) #--> This will fetch the value of Index numbers starting from 2 till end i.e. llo World this is python

print("The values are:- ",s[:8]) #--> This will fetch the values of index number starting from 0 till 7 i.e. Hello Wo

print("Jumped values are:- ",s[::3]) #--> This will fetch the values after JUMPING 2 values (One less then mentioned) starting from 0. i.e. HlWltssyo

print("Length of string:- ",len(s)) #--> This will provide TOTAL LENGTH of string. IT WIL START COUNTING FROM 1 and NOT FROM 0. THUS o/p will be 26


s= "       Hello World this is python     " #--> Here gap/whitespace is available at starting and end of string. This is to be removed
s=s.strip()   #--> This removes any whitespace/gap available at beginning or the end of the string. NOT MIDDLE SPACES, ONLY REMOVES GAP DURING START AND END OF STRING
print("strip-",s)


s= "HEY HOW ARE YOU ?"
s=s.lower() #---> This will CONVERT STRING TO LOWER CASE (Small aplhabets) of string, if it was written in UPPER CASE (Capital Letters) i.e.hey how are you ?
print("lower:- ",s)

s= "hey how are you ?"
s=s.upper()  #-->This will CONVERT STRING TO UPPER CASE (Capital aplhabets) of string, if it was written in LOWER CASE (small Letters) i.e."HEY HOW ARE YOU ?"
print("upper:- ",s.upper())


s= "HEY, I am FINE HOW are you?" #--> This is mix of small and capital letters
s=s.replace('HEY', 'HI')  #--> This will REPLACE HEY with HI. Remember as our HEY in "s" is in CAPITAL letters, we should enter it in capitals only. otherwise it will not identify and print as it is.
print("After replacement new line becomes:- ",s)
# NOTE THAT HERE WE CAN REPLACE ONLY ONCE. FOR MULTIPLE REPLACEMENT WE NEED TO TYPE s=s.replace('WORD TO BE REPLACED', 'NEW WORD')in new line again

s= "Hello World @this is @python"
s=s.split('@') #---> This will split the sentence where @ symbol is marked. We can use any other symbol too. OUTPUT will be:- ['Hello World ', 'this is ', 'python']
print("split:- ",s)

s= "Hi, World $is $very cruel. Either accept it $or fight it back"
s=s.split('$')    #---> OUTPUT IS ['Hi, World ', 'is ', 'very cruel. Either accept it ', 'or fight it back']
print("split:- ",s)


s= "hey how are you ?"
s=s.capitalize()  #--> This will only CAPITALIZE THE FIRST CHARACTER OF THE FIRST WORD IN LINE and NOT EVERY STARTING WORD. OUTPUT:- Hey how are you ?. Here only "H" is capitalized.
print(" Capitalized Line is:-",s)

s= "hey how are you ?"
s=s.title()  #--> This will only CAPITALIZE THE FIRST CHARACTER OF ALL THE WORDS IN THE LINE. OUTPUT:- Hey How Are You ?. If the word contains a number or a symbol, the first letter after that will be converted to upper case.
print(" Capitalized Line is:-",s)

s = ("John", "Peter", "Vicky")
x = "#".join(s) #--> This will JOIN the "s" BUT having HASTAG in between (John#Peter#Vicky). REMOVE HASH and simple add space between QUOTES that will look good.
print(x)

s1='HeLlo WoRld'
print("swapping:- ",s1.swapcase()) #--> This will SWAP the cases, i.e LOWER CASE KO UPPER CASE BANYAEGA & UPPER CASE KO LOWER CASE BANAYEGA. RESULT:- hElLO wOrLD

s="helloworld123"
print("count:- ",s.count('l',0,14))  #--> .count(value, start, end). This COUNTS the number of times a specified value appears in the string.Here we tried to find how many times "l" is there.
# AGAR HUMKO START SE END TAK JANA HAI TOH ALAG ALAG TARIKE SE LIKH SAKTE HAI.FOR E.G.:-
#print("count:- ",s.count('l',0,-1)) -->(ZERO se start karke -1 tak yani last value tak jayega)
#print("count:- ",s.count('l',0)) --> End value mention na bhi karo fir bhi woh end tak hi jayega


s= "Hello World this is python"
print("endswith or not:- ",s.endswith('python',2,27)) #--> This will CHECK IF THE STRING IS ENDING WITH THE WORD "python" OR NOT.  It returns TRUE if the string ends with the specified value, otherwise False.
                     # endswith(value, start, end)..--> LOWER CASE aur UPPER CASE KA DHYAN RAKHNA HAI. Yahan python lower case mein hai...agar humnein UPPER CASE mein likh diya to FALSE ayega.

s= "Hello World this is python"
print("find the value:- ",s.find('I',0,27)) #--> This FINDS THE FIRST OCCURENCE of the specified value "I". It will returns -1 if the VALUE IS NOT FOUND. As I is in UPPER CASE thus it will show -1
	 # string.find(value, start, end)
print("find the value:- ",s.find('i',0,27)) #--> Here "i" is in lower case thus it will show 14. Because 'i' has appeared first time on index value 14.



s="This is {a} class and class no  is {b}"
print("Newly formated line is:-",s.format(a="Python",b="205-A"))  #--> This FORMATS/REPLACES the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. Yani curly bracket mein jo likha hai uski jagah .format ki bracket wali values daldo.


s= "my name is john234"
print("It is alphanumeric:- ",s.isalnum()) #--> This will returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
# (space)!#%&? are NOT CONSIDERED alphanumeric. In 's' as space is there between words thus it will return false

s= "mynameisjohn234"
print("It is alphanumeric:- ",s.isalnum()) #--> Here no space is there between words thus it will return true


s1="hello world"
print("All are alphabets:- ",s1.isalpha()) #--> This returns True if all the characters are ALPHABETS letters (a-z). Here it will return FALSE as there is SPACE between 'hello' and 'world'

s1="helloworld"
print("All are alphabets:- ",s1.isalpha()) #-->Here it will return TRUE as there is NO SPACE between 'hello' and 'world


s1='1234 6366'
print("isdigit:- ",s1.isdigit()) #--> This returns True if all the characters ARE DIGITS, otherwise False. Here it will return FALSE as there is SPACE between '1234' and '6366'


s1='12346366'
print("isdigit:- ",s1.isdigit()) #-->Here it will return TRUE as there is NO SPACE between '1234' and '6366'

s1="hello World 1213  %$###@"
print("All are lower case:- ",s1.islower()) #--> This returns True if all the characters are in lower case, otherwise False. NO EFFECT OF SPACES,SPECIAL CHARACTERS OR NUMBERS.
#This will return FALSE because 'W' is UPPER CASE.

s1="hello world 1213  %$###@"
print("All are lower case:- ",s1.islower()) #-->This will return TRUE because 'W' is LOWER CASE. NO EFFECT OF SPACES,SPECIAL CHARACTERS OR NUMBERS.


s1="HELLLO WORLD 1213  %$###@"
print("All are Upper case:- ",s1.isupper()) #--> This returns True if all the characters are in upper case, otherwise False. NO EFFECT OF SPACES,SPECIAL CHARACTERS OR NUMBERS.

s1="HeLlO WOrLd 1213  %$###@"
print("All are Upper case:- ",s1.isupper()) #--> This will return FALSE beacuse all ar not in upper case.


s1='1234366'
print("All are numbers:- ",s1.isnumeric())  #-->This will return True if ALL CAHARACTERS ARE NUMERIC (0-9), otherwise False.SPACES AND SPECIAL CHARACTERS WILL SHOW FALSE, THUS NOT PERMITTED
#Here above will show true because all are numerics

s1='123@4366'
print("All are numbers:- ",s1.isnumeric()) #--> This will return FALSE because special character is present.

s1=' a'
print("isspace:- ",s1.isspace()) #-->This returns True if all the characters in a string are whitespaces, otherwise False. PURA WHITE/BLANK HONE CHAYIYE. KUCH BHI PRINT MILA TOH FALSE AYEGA
#Here "a" is there, Thus it will show FALSE

s1=' '
print("isspace:- ",s1.isspace()) #--> This will show TRUE because nothing is available in s1


s1='Hello world'
print(" Initial characters are titlecase:- ",s1.istitle()) #--> This returns True IF ALL WORDS IN A TEXT START WITH A UPPER CASE, AND REST OF THE WORD ARE LOWER CASE LETTERS, otherwise False.
#Here, in above world DOESNT START WITH CAPITAL "W". Thus, answer will be false.


s1='Hello World'
print("Initial characters are titlecase:- ",s1.istitle()) #--> Here, Hello and World both START WITH CAPITAL LETTERS. Thus, answer will be TRUE. Agar koi ek aur letter capital hogaya toh false ho jayega.
'''

s1='a85_abc_23'
print("It is a valid identifier:- ",s1.isidentifier())  #--> This returns True if the string is a valid identifier, otherwise False. NO SPECIAL CHARACTERS ARE PERMITTED
# A STRING IS CONSIDERED A VALID IDENTIFIER IF IT ONLY CONTAINS ALPHANUMERIC LETTERS (A-Z) AND (0-9), OR UNDERSCORES (_).
#A VALID IDENTIFIER CANNOT START WITH A NUMBER, OR CONTAIN ANY SPACES.

s1='2a85_abc_23'
print("It is a valid identifier:- ",s1.isidentifier()) #--> FALSE. CANNOT START WITH NUMBER

s1='  85_abc_23'
print("It is a valid identifier:- ",s1.isidentifier()) #--> FALSE. CANNOT START WITH SPACE/GAP

s1='@85_abc_23'
print("It is a valid identifier:- ",s1.isidentifier()) #--> FALSE. CANNOT START WITH SPECIAL CHARACTER

s1='_85_abc_23'
print("It is a valid identifier:- ",s1.isidentifier()) #--> TRUE. IT CAN START WITH UNDERSCORE.


