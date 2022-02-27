#Q1
print("Ans1")
def TowerOfHanoi(n , from_rod, to_rod, middle_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, from_rod, middle_rod, to_rod)
	print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
	TowerOfHanoi(n-1, middle_rod, to_rod, from_rod)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print()

#Q2
print("Ans2")
from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))

print("Using iterative procedures")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
	print()
print("\n\n")

print("Using recurssions")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    print('  '*(originalength-n), end='')

    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')

        start = start * (n - i) // i
    
    print()
pascal_triangle(n)
print()




#Q3
print("Ans3")
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Q = int1 // int2
R = int1 % int2

#a
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Q))
print(callable(R))

#part b
if (Q == 0):
    print("b. The quotient is zero")
if (R == 0):
    print("b. The reminder is zero")
if (Q != 0 and R != 0):
    print("b. All the values are non zero")

#part c
part_c_list = [Q + 4, R + 4, R + 5, Q + 5, R + 5, Q + 6, R + 6]

result = []
for i in range(len(part_c_list)):
    if part_c_list[i] > 4:
        result.append(part_c_list[i])
print(f"c. Filtered out numbers that are greater than 4 are : {result}")

#part d
setresult = set(result)
print("d. Set:",setresult)

#part e
immutableSet = frozenset(setresult) 
print("e Immutable set:",immutableSet)

#part f
print("f. Hash value of the max value from the above set:", hash(max(immutableSet)))
print()

#Q4
print("Ans4 ")
class Student:
    def __init__(self, student,roll_number):
        self.name = student
        self.roll_number = roll_number
    
    def __del__(self):
        print("Object destroyed")

student_1 = Student("Pratham_Banga", 20103015)
print("Object created")
print(f"The name of the student it {student_1.name} and SID is {student_1.roll_number}.")
del student_1
print()

#Q5
print("Ans5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#a. for updating salary
employee1.salary = 70000
print(f"a. The updated salary of {employee1.name} is {employee1.salary} ")
#b. for deleting a record
print("b. Record of Viren deleted", end='')
del employee3
print()

#Q6
print("Ans6")
word =input("Enter the word: ")
word=word.lower()


testword = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
testword=testword.lower()
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't exact, friendship is fake")
        return
    ans = input("Does the word makes sense?(y or n)")

    if ans == 'y' or ans == 'Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans == 'N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input, try again with y or n ")
        userinput()
userinput()