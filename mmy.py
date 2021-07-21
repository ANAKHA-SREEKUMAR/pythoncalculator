print("### calculator ###")
x=int(input("enter first number:"))
y=int(input("enter second number:"))
print("a.sum")
print("b.sub")
print("c.mul")
print("d.div")
z=input("choose from above:")
print(z)
if z=="a":
    print("answer=",x+y)
elif z=="b":
    print("answer=",x-y)
elif z=="c":
    print("answer=",x*y)
elif z=="d"and y!=0:
    print("answeer=",x/y)
else:
    print("invalid")
