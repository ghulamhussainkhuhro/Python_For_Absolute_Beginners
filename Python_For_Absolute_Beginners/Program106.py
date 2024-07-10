# Multiple Inheritance in python

class A:
    varA = "Welcome to class A..."

class B:
    varB = "Welcome to class B..."

class C(A,B):
    varC = "Welcome to class C..."

c = C()
print(c.varA)
print(c.varB)
print(c.varC)