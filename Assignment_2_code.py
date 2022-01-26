#quetion 1
string1="Python is a case sensitive language"
print("<A>THE LENGTH OF STRING IS:-",len(string1))
print("<B>THE REVERSED STRING IS :-",string1[-1::-1])
string2=string1[10:26] 
string2.replace("a case sensitive","object oriented") 
print("<E>THE INDEX OF SUBSTRING a is ",string1.find('a'))
print("<F>THE ORIGINAL STRING AFTER REMOVING WHITESPACES IS",string1.replace(" ",""))
print()

#question 2
name=input("ENTER YOUR NAME")
sid=int(input("ENTER YOUR SID"))
dept=input("ENTER YOUR DEPARTMENT")
cgpa=float(input("ENTER YOUR CGPA"))
print("Hey %s,"%name,"Here!")
print("My SID is %d" %sid)
print("I am from %s"%dept,"and my CGPA is %f"%cgpa)
print()

#question 3
a=57
b=13
print("a. ",a&b)
print("b. ",a|b)
print("c. ",a^b)
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)
print()

#quention 4
numbers = [int(x) for x in input().split()]
min_num = numbers[0]
for x in numbers:
	if x < min_num:
		min_num = x

print("minimum no. is :-"min_num)
print()

#quetion 5
string = input()
if "name" in string:
	print("yes")
else: 
	print("no")
print()

#question 6
x,y,z = [int(x) for x in input().split()]
if x + y < z:
	print("no")
elif y + z < x:
	print("no")
elif x + z < y:
	print("no")
else:
	print("yes")