def areacalculator():
a = input("enter the shape that need to calculate:")
    area = 0
    p = 3.14
    if a == "square":
        side = int(input("enter the value of side: "))
        area = area + (side ** 2)
    elif a == "circle":
        b = int(input("enter the value of r: "))
        area = area + (2 * p * b)
    elif a == "rectangle":
        length = int(input("enter the value of length: "))
        width = int(input("enter the value of length: "))
        area = area + (length * width)
    elif a == "triangle":
        base = int(input("enter the value of base: "))
        height = int(input("enter the value of height: "))
        area = area +(0.5 * base * height)
    else:
        print("select a valid shape")
    print("%.2f" % area)
areacalculator()

#1.2

import math
def mean(arr):
    mean = 0
    sum = 0
    for i in range(len(arr)):
        mean += (arr[i]/len(arr))
        sum += arr[i]
    print(sum, ',', round(mean, 3))
z = [15, 25, 21, 64, 34, 97, 84, 61]
x = [54, 0, 31, 74, 89, 9, 0]
c = [52, 40, 49, 94, 3, 70, 69, 4, 35, 21, 5]
mean(z)
mean(x)
mean(c)

#2.1
import math
def hexagon(side):
    return 6 * areaTriangle(side)
def areaTriangle(side):
    return (math.sqrt(3) / 4) * math.pow(5, 2)
z = float(input("enter the side: "))
print("%.2f" % hexagon(z))

#2.2
def area(z, x):
    area = (z*x)
    print(area)
z = int(input('The lenght of the first side of first rectangle: '))
x = int(input('The lenght of the second side of first rectangle: '))
area(z, x)
z1 = int(input('The lenght of the first side of first rectangle: '))
x1 = int(input('The lenght of the second side of first rectangle: '))
area(z1, x1)
z2 = int(input('The lenght of the first side of first rectangle: '))
x2 = int(input('The lenght of the second side of first rectangle: '))
area(z2, x2)

#3.1
import math
def cPow(lst):
    z = math.sqrt(math.pow(lst[0],2)+math.pow(lst[1],2))
    x = math.sqrt(math.pow(lst[2],2)+math.pow(lst[3],2))
    print("hypotenuses of 1 triangle =",z)
    print("hypotenuses of 2 triangle =",x)
    if z > x:
        print("the hypotenus or 1st triangle largest:",x)
    elif z == x:
        print("they are equal")
    else:
        print("the hypotenus or 2nd triangle largest:",x)
tr=[]
print("enter the sides of triangle")
for i in range(2):
    print("for",i+1,"triangle")
    tr.append(float(input("the 1st side: ")))
    tr.append(float(input("the 2st side: ")))
cPow(tr)

#3.2
def sort(str):
    return ''.join(sorted(str))
z = str(input('Enter the string: '))
print (sort(z))

#4.1
import math
def divide(lst):
    list_new1 = list(map(int, arr[0].split('/')))
    list_new2 = list(map(int, arr[1].split('/')))
    return reduceF([list_new1[0] * list_new2[1], list_new1[1] * list_new2[0]])
def reduceF(lst):
    divider, q, w = gcdEuclid(lst[0], lst[1])
    return [i / divider for i in lst]
def gcdEuclid(a, b):
    if a == 0:
        return b, 0, 1
    gcd, q1, w1 = gcdEuclid(b % a, a)
    q = w1 - (b // a) * x1
    w = q1
    return gcd, q, w
arr = []
for i in range(2):
    arr.append(input("enter the fraction n" + str(i + 1) + ": "))
result = divide(arr)
print(result[0], "/", result[1])

#4.2
def isInside(q, w, rad, z, x):
    if ((z - q) * (z - q) +
            (x - w) * (x - w) <= rad * rad):
        return True
    else:
        return False
z = 11
x = 12
q = 0
w = 1
rad = 2
if isInside(q, w, rad, z, x):
    print("Inside")
else:
    print("Outside")

#5.2
def printt(z):
    for i in z:
        print(i, "end" = ',')
def division(z):
    x = []
    for i in range(1, (z+1)):
        if z%i==0:
            x.append(i)
    printt(x)
z = int(input('Enter the number: '))
division(z)

#6.1
def gcdEuclid(q, w):
    if q == 0:
        return w, 0, 1
    gcd, z1, x1 = gcdEuclid(w % q, q)
    z = x1 - (w // q) * z1
    x = z1
    return gcd, z, x
def lcm(q, w):
    gcd, z, x = gcdEuclid(q, w)
    return (q * w) / gcd
q, w = list(map(int, input("enter a,b: ").split()))
gcd, x, y = gcdEuclid(q, w)
print("GCD is:", gcd)
print("LCM is:", lcm(q, w))

#6.2
import math
def quadrilateralArea(lst, diagonal):
    h1 = 2 * (areaTriangle(lst[0], lst[1], diagonal) / diagonal)
    h2 = 2 * (areaTriangle(lst[2], lst[3], diagonal) / diagonal)
    area = 0.5 * diagonal * (h1 + h2)
    return area
def areaTriangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
x = list(map(float, input("enter 4 sides one after one: ").split()))
d = float(input("enter the diagonal: "))
print("area of quadrilateral: ", quadrilateralArea(x, d))

#7.1
import math
def quadrilateralArea(lst):
    q = (lst[0] + lst[1] + lst[2] + lst[3]) / 2
    area = math.sqrt(((q - lst[0]) * (q - lst[1]) * (q - lst[2]) * (q - lst[3])) - (
                lst[0] * lst[1] * lst[2] * lst[3] * math.pow(math.cos(math.pi / 2), 2)))
    return area
x = list(map(int, input("enter 4 sides one after one: ").split()))
print("area of quadrilateral: ", quadrilateralArea(x))

#7.2
def o(a):
    if a > 0:
        return o(a)
    else:
        return ('There is no way.')
a = int(input('Enter the number: '))
print(o(a))

#8.1
def division(a):
    for i in range(a):
        if divide(i) == True:
            print(i)
def divide(a):
    temperature = a
    while (temperature > 0):
        digit = temperature % 10
        if ((digit != 0 and a % digit == 0) == False):
            return False
        temperature = temperature // 10
    return True
a = int(input("enter the numb: "))
division(a)

#8.2
def swap(lst):
    lst[0],lst[len(lst)-1] = lst[len(lst)-1],lst[0]
    return lst
input("the length of array: ")
list_new = list(map(int, (input("Enter the array: ")).split()))
print("original array: ",list_new)
print("swapped: ",swap(list_new))

#9.1
def Sum(n):
    sum = 0
    for digit in str(n):
    sum += int(digit)
    return sum
def sumC(n, sum):
    repeat = -1
    while n >= 0:
        n -= sum
        repeat += 1
    return repeat
n = int(input("Enter the number: "))
sum = Sum(n)
print(sum)
print(sumC(n, sum))

#9.2
import statistics
def multiplyList(myList):
	result = 1
	for x in myList:
		result = result * x
	return result
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
print("The product of the elements in 1 list =", multiplyList(list1))
print("The product of the elements in 2 list =", multiplyList(list2))
print("The product of the elements in 3 list =", multiplyList(list3))
print("The arithmetic mean of 1 list =", statistics.mean(list1))
print("The arithmetic mean of 2 list =", statistics.mean(list2))
print("The arithmetic mean of 3 list =", statistics.mean(list3))

#10.1

interval = []
for i in range(210, 231):
interval.append(i)
res = [sub for sub in interval if len(set(str(sub))) == len(str(sub))]
print(str(res))

#10.2
string = input("enter the str: ")
q = string.split()[::-1]
w = []
for i in q:
w.append(i)
print(" ".join(w))

#11.1
def prime(a):
    if n <= 1:
        return False
    for i in range(3, a):
        if a % i == 0:
            return False
    return True
def print(a):
    for i in range(a, a * 2):
        if prime(i):
            print(i, end " ")
a = int(input("enter the a: "))
print(a)

#11.2
list1 = [10, 250, 20, 4, 100, 45, 99]
print(list1)
print("maximum of list1:", max(list1))
list2 = [15, 86, 54, 320, 112, 55, 74]
print(list2)
print("maximum of list2:", max(list2))
index1 = list1.index(max(list1))
index2 = list1.index(max(list2))
list1[index1], list2[index2] = list2[index2], list1[index1]
print(list1, list2)

#12.1
def findFriendly(n):
    f = 0
    for ch in range(n):
        if ch != f:
            s1 = 0
            for i in range(1, ch // 2 + 1):
                if ch % i == 0:
                    s1 += i
            s2 = 0
            for j in range(1, s1 // 2 + 1):
                if s1 % j == 0:
                    s2 += j
            if s2 == ch != s1:
                print(ch, s1)
                f = s1
n = int(input("enter the numb: "))
findFriendly(n)

#12.2
import math
def median(a, b, c):
    median = math.sqrt(2 * (b * b + c * c) - a * a) / 2
    return median
print("enter 3 sides:")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if abs(a - b) >= c | a + b <= c:
    print("impossible triangle")
print("medians of original triangle:")
mA = median(a, b, c)
mB = median(b, a, c)
mB = median(c, a, b)
print(ma, mb, mc)
print("medians of created triangle:")
mmA = median(mA, mB, mB)
mmB = median(mB, mA, mC)
mmC = median(mC, mA, mB)
print(mmA, mmB, mmC)

#13.1
def armStrong(n):
    for num in range(1, 1000):
        order = len(str(num))
        sum = 0
        a = num
        while a > 0:
            digit = a % 10
            sum += digit ** order
            a //= 10
        if num == sum:
            print(num)
n = int(input("enter the n: "))
armStrong(n)
    
#13.2
def acos(x, y):
    return x / ((x * x + y * y) ** 0.5)
x1, x2 = map(float, input().split())
y1, y2 = map(float, input().split())
z1, z2 = map(float, input().split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx:
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx:
    acosz = acosz
    res = [z1, z2]
print(*res)
n = 3
res = [tuple(map(float, input().split())) for i in range(n)]
rcos = [acos(*res[i]) for i in range(n)]
k = rcos.index(max(rcos))
print(res[k])

#14.1
def countDivisors(a):
    result = []
    i = 1
    while i * i < a + 1:
        if a % i == 0:
            result.append(i)
            if i != a // i:
                result.append(a // i)
        i += 1
    return sorted(result)
def function(m, n):
    div = []
    for num in range(m, n + 1):
        frac = countDivisors(num)
        div.append((len(frac), -num, frac[-2:]))
    div.sort()
    print(-div[-1][1], 'consist', div[-1][0], 'divisors')
function(2, 4682192)

#15.1
def findPrime(n):
    arr = [True for _ in range(n + 1)]
    i = 1
    while 2 * i * (i + 1) < n:
        j = i
        while j <= (n - i) / (2 * i + 1):
            arr[2 * i * j + i + j] = False
            j = j + 1
        i = i + 1
    for i in range(1, n + 1):
        elem = arr[i]
        if elem:
            prime = 2 * i + 1
            if prime > n: break
            a = bin(prime)[2:]
            b = bin(prime)[2:][::-1]
            if a == b:
                print(prime, end ' ')
n = int(input("enter the numb: "))
findPrime(n)