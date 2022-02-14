#QUESTION1
print("Q1")
inputstr = input("ENTER ANY STRING: ")
a = inputstr.split() 
dict={}
if len(a)==1:   
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:           
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print()



#QUESTION2
from subprocess import list2cmdline


print("Q2")
def Next_Date():
    list1=[1,3,5,7,8]
    list2=[4,6,9,11]
    list3=[2]
    list4=[12]
    while(True):     
        day=int(input("ENTER THE DAY: "))
        if(1<=day<=31):
            break
        else:
            print("Please Enter a valid day")
    while(True):    
        month=int(input("ENTER THE MONTH OF THE YEAR: "))
        if(1<=month<=12):
            break
        else:
            print("Please Enter a valid month")
    while(True):                
        year=int(input("ENTER THE YEAR: "))
        if(1800<=year<=2025):
            break
        else:
            print("Please Enter year from 1800 to 2025 only")
    if month in list1 :    
        if(day==31):
            day=1
            month=month+1
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
    
    elif month in list2 :
        if(day==30):
            day=1
            month=month+1  
            print(day,"/",month,"/",year)   
        elif(day<30):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN") 
            Next_Date()      
    elif month in list3:
        if(year % 4 == 0):  
            if(day==29):
                day=1
                month=month+1
                print(day,"/",month,"/",year)
            elif(day<29):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
        else:
            if(day==28):
                day=1
                month+=1
                print(day,"/",month,"/",year)
            elif(day<28):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
    elif month in list4:
        if(day==31):
            day=1
            month=1
            year+=1  
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1;
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
        
    else:
        print("INVALID DATE TRY AGAIN")
        Next_Date()
Next_Date()
print()



#QUESTION3
print("Q3")
inp_list = input('Enter elements of a list separated by space ')
user_list = inp_list.split()

print('list: ', inp_list)


for i in range(len(user_list)):

    user_list[i] = int(user_list[i])
square_list =[(user_list[i], user_list[i]**2) for i in range(len(user_list))]

print(squarelist)

print("\n")


#QUESTION4
print("Q4")

def input_point():
    point = int(input("Enter Grade Point: "))
    
    if point>10 or point<4:
        print("Invalid grade point! Try Again")
        point = input_point()
    return point
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print()


#QUESTION5
print("QUESTION 5")
x = 6
for i in range(x):
    
    for j in range(i):
        print(' ', end='')
    
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')
    print()
print()

#QUESTION6
print("Q6")
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')


print("<a>",students)

print("<b>",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

print("<c>",{k:v for k,v in sorted(students.items())})

sid = int(input("Search Name with SID: "))

print("<d>",students[sid])

#QUESTION7
print("Q7")

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
no_of_terms = int(input("Enter the no. of terms in series: "))
if no_of_terms <= 0:    
   print("Enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(fibo(i))
       sum_ = sum_ + fibo(i)
avg = float(sum_ / no_of_terms)
print("AVERAGE OF RESULTANT FIBONACCI SERIES IS",avg)


#QUESTION8
print("Q8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)


Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set)

Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set)

Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)

Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)
"""

END
by pratham banga
20103015

"""
