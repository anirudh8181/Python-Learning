#-----------------variables------------------------------------

# #string
first_mame="ani"

#int
x=3

#float
y=3.14

#boolean
is_there=False
is_there1=True


print(f"hi , hey...{first_mame} it is {x} but {y} the boolean {is_there} {is_there1}")

 
 #------------Type casting---------------------------------------------------------------

name="bro"
age=22
is_employee=True

age=float(age)
print(type(age))

name=bool(is_employee)
print(name)

#------------------user input---------------------------------------------

z_1=int(input("enter an intger :"))
print(z_1)


y_1=float(input("enter an float intger :"))
print(y_1)

print("the sum is = ",z_1+y_1)

#----------arithematic math----------------------------


q=1.23
q=q**2
#q**=2 (augumented type expression)
print("the arithmatic operation\n",q) 

#-----------------------------------------------------------
x=int(input("enter :"))
print(True if x>20 else False)


