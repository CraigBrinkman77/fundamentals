for x in range(151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101,1):
    if x % 10 == 0:
        print("coding")
    elif x % 5 == 0:
        print("coding dojo")
    else:
        print(x)

total = 0
for x in range(500000):
    if x % 2 != 0:
        total = total + x

print(total)

for x in range(2018,0,-4):
    print(x)

lowNum=2
highNum=9
mult=3
for x in range(lowNum, highNum + 1, 1):
    if x % mult == 0:
        print(x)
    



