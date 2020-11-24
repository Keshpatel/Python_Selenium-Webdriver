x = int(input("Please enter the value of x"))

if x < 0:
    print("x is nagative number")
elif x > 0:
    print("x is positive number")
elif x == 0:
 print("not defined")

if True:
    print("PASS")
else:
    print("FAIL")

if 10 > 5:
    print("HI")

a = 100
b = 200
c = 300

if a > b and a > c:
    print("a is the highest number")
elif b>c:
    print("b is the highest number")
else:
    print("c is the highest number")

total = int(input("enter the total value:"))
if (total < 100):
    total = total + 20
elif (total >= 100 and total<=500):
    total = total + 50
else:
    total = total + 100

print(total) # no concat
print("total ="+ str(total)) #str method
print(f'{"total value="}{total}') # i strings
