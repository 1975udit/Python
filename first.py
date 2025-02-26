print("Hello")

# name = input("Enter your name :")
# print("hello ",name)

l = [1,10,30,2,"udit"]  # list -> mutable
l.remove("udit")
# print(l)
# l.sort()
# print(l)

t = (1,3,2,5,4,"udit")
# print(t)
# t.remove("udit")   This give error bcz tuple is immutable like strings

s = {3,4,5,5,5,7,8}   
# print(s)      # set never stores duplicate values
# s.remove(5)
# print(s)      # But sets are mutable like the list 
# In set pop() operation remove the random element not the last


dict1 = {1 : "a", 2 : "b", 3 : "c", 4 : "d"}
print(dict1[1])   # you can use .get() inplace of that to caure form error if key is not present
dict1[5] = "e"   # dict are mutable
# print(dict1) 
print(dict1.get(6))   # return None

# Switch Case

a = 5
match(a):
    case 1 :
        print("Case 1")
    case 2 : 
        print("case 2")
    case 5 : 
        print("case 5")
    case _:
        print("Default Case")

# n = int(input("Enter the Number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

def Fun():
    print("This is a function")
# Fun()

def fString(name):
    str = f'This is {name}'  # fstring example
    print(str)
# fString("udit")

try :
   n = int(input("Enter the input :"))
except Exception as e:
   print(e)
finally:
    print("This is error handling")