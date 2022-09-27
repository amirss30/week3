#1
import math
print("1: Area of the Circle");
choice = int(input(""))
if choice==1:
    radius = float(input("Enter the radius of the Circle: "))
    area = math.pi*pow(radius,2)
    print(f"The area of the circle with radius {radius} is : {round(area,2)}")
#1(2)
def findTriplet(a1, a2, a3,
                n1, n2, n3, sum):
    for i in range(0, n1):
        for j in range(0, n2):
            for k in range(0, n3):
                if (a1[i] + a2[j] +
                        a3[k] == sum):
                    return True

    return False
a1 = [1, 2, 3, 4, 5]
a2 = [2, 3, 6, 1, 2]
a3 = [3, 2, 4, 5, 6]
sum = 9
n1 = len(a1)
n2 = len(a2)
n3 = len(a3)
print("Yes") if findTriplet(a1, a2, a3,
                            n1, n2, n3,
                            sum) else print("No")
#2
import math
def hexagonArea(s):
    return ((3 * math.sqrt(3) *
            (s * s)) / 2);
if __name__ == "__main__" :
    s = 4
    print("Area:","{0:.4f}" .
           format(hexagonArea(s)))
    #2(2)
    def rectangle(x, y):
        area = x * y
        print(str(area * 3), " area of the 3 Rectangles")
    width = int(input("enter the width: "))
    height = int(input("enter the height : "))
    rectangle(width, height)
    #3
    from math import sqrt
    print("Input lengths of shorter triangle sides:")
    x = float(input("x: "))
    y = float(input("y: "))
    z = sqrt(x ** 2 + y ** 2)
    print("The length of the hypotenuse is:", z)
#3(2)
s ="justforfun"
li = []
l = len(s)
for i in range (0,l):
    li.append(s[i])
for i in range(0,l):
    for j in range(0,l):
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
j=""
for i in range(0,l):
    j = j+li[i]
print(j)
#4
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
def lowest(den3, num3):
    common_factor = gcd(num3, den3)
    den3 = int(den3 / common_factor)
    num3 = int(num3 / common_factor)
    print(num3, "/", den3)
def addFraction(num1, den1, num2, den2):
    den3 = gcd(den1, den2)
    den3 = (den1 * den2) / den3
    num3 = ((num1) * (den3 / den1) +
            (num2) * (den3 / den2))
    lowest(den3, num3)
num1 = 1; den1 = 500
num2 = 2; den2 = 1500
print(num1, "/", den1, " + ", num2, "/",
    den2, " is equal to ", end = "")
addFraction(num1, den1, num2, den2)
#4(2)
import math
def preprocess(p, x, y, n):
    for i in range(n):
        p[i] = x[i] * x[i] + y[i] * y[i]
    p.sort()
def query(p, n, rad):
    start = 0
    end = n - 1
    while ((end - start) > 1):
        mid = (start + end) // 2
        tp = math.sqrt(p[mid])
        if (tp > (rad * 1.0)):
            end = mid - 1
        else:
            start = mid
    tp1 = math.sqrt(p[start])
    tp2 = math.sqrt(p[end])
    if (tp1 > (rad * 1.0)):
        return 0
    else if (tp2 <= (rad * 1.0)):
        return end + 1
    else:
        return start + 1
if __name__ == "__main__":
    x = [ 1, 2, 3, -1, 4 ]
    y = [ 1, 2, 3, -1, 4 ]
    n = len(x)
    p = [0] * n
    preprocess(p, x, y, n)
    print(query(p, n, 3))
    print(query(p, n, 32))
    #6
import math
def maxArea(a, b, c, d):
    semiperimeter = (a + b + c + d) / 2
    return math.sqrt((semiperimeter - a) *
                     (semiperimeter - b) *
                     (semiperimeter - c) *
                     (semiperimeter - d))
a = 1
b = 2
c = 1
d = 2
print("%.2f" % maxArea(a, b, c, d))
#7
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")
#7(2)
def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")
n = 33
decToOctal(n)
#8
max_num = 20
n = 1
print("Numbers not divisible by 2 and 3")
while n <= max_num:
    if n % 2 != 0 and n % 3 != 0:
        print(n)
    n = n + 1
#8(2)
def repeat_times(n):
  n_str = str(n)
  while (n > 0):
    n -= sum([int(i) for i in list(n_str)])
    n_str = list(str(n))
  return n
print(repeat_times(9))
print(repeat_times(20))
print(repeat_times(110))
print(repeat_times(5674))
#10
string = "i love python"
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))
#10(2)
items = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
print( ",".join(items))
#11
import sys
N = 4
M = 4
def findMax(mat):
    maxElement = -sys.maxsize - 1
    for i in range(N):
        for j in range(M):
            if (mat[i][j] > maxElement):
                maxElement = mat[i][j]
    return maxElement
if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
           [25, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    print(findMax(mat))
    #11(2)
    import math
    def sumofFactors(n):
        res = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            count = 0;
            curr_sum = 1;
            curr_term = 1
            while (n % i == 0):
                count += 1
                n = n // i
                curr_term *= i
                curr_sum += curr_term
            res *= curr_sum
        if (n >= 2):
            res *= (1 + n)
        return res
    def gcd(a, b):

        if (a == 0):
            return b
        return gcd(b % a, a)
    def checkFriendly(n, m):
        sumFactors_n = sumofFactors(n)
        sumFactors_m = sumofFactors(m)
        gcd_n = gcd(n, sumFactors_n)
        gcd_m = gcd(m, sumFactors_m)
        if (n // gcd_n == m // gcd_m and
                sumFactors_n // gcd_n == sumFactors_m // gcd_m):
            return True

        else:
            return False
    n = 6;
    m = 28
    if (checkFriendly(n, m)):
        print("Yes")
    else:
        print("No")
        #13
        def isArmstrong(val: int) -> bool:
            parts = [int(_) for _ in str(val)]
            counter = 0
            for _ in parts:
                counter += _ ** 3
            return (counter == val)
        print(isArmstrong(153))
        print(isArmstrong(1253))
        #13(2)
        def lineFromPoints(P, Q):
            a = Q[1] - P[1]
            b = P[0] - Q[0]
            c = a * (P[0]) + b * (P[1])
            if (b < 0):
                print("The line passing through points P and Q is:",
                      a, "x - ", b, "y = ", c, "\n")
            else:
                print("The line passing through points P and Q is: ",
                      a, "x + ", b, "y = ", c, "\n")
        if __name__ == '__main__':
            P = [3, 2]
            Q = [2, 6]
            lineFromPoints(P, Q)
            #14
import math
            def countDivisors(n):
                count = 0
                for i in range(1, int(sqrt(n) + 1)):
                    if n % i == 0:
                        if n / i == i:
                            count += 1
                        else:
                            count += 2
                return count
            def MaximumDivisors(X, Y):
                result = 0
                maxDivisors = 0
                arr = []
                for i in range(Y - X + 1):
                    arr.append(0)
                for i in range(X, Y + 1):
                    Div = countDivisors(i)
                    arr[i - X] = Div
                    maxDivisors = max(Div, maxDivisors)
                for i in range(Y - X + 1):
                    if arr[i] == maxDivisors:
                        result += 1
                return result
            if __name__ == "__main__":
                X, Y = 1, 10
                print(MaximumDivisors(X, Y))
                #14
def leftmostSetBit(x):
    count = 0
    while (x):
        count += 1
        x = x >> 1
    return count
def isBinPalindrome(x):
    l = leftmostSetBit(x)
    r = 1
    while (l > r):
        if (isKthBitSet(x, l) != isKthBitSet(x, r)):
            return 0
        l -= 1
        r += 1
    return 1
def findNthPalindrome(n):
    pal_count = 0
    i = 0
    for i in range(1, INT_MAX + 1):
        if (isBinPalindrome(i)):
            pal_count += 1
        if (pal_count == n):
            break
    return
if __name__ == "__main__":
    n = 9
    print(findNthPalindrome(n))
    #15
    import math
    def distance(x1, y1, z1, x2, y2, z2):
        d = math.sqrt(math.pow(x2 - x1, 2) +
                      math.pow(y2 - y1, 2) +
                      math.pow(z2 - z1, 2) * 1.0)
        print("Distance is ")
        print(d)
    x1 = 2
    y1 = -5
    z1 = 7
    x2 = 3
    y2 = 4
    z2 = 5
    distance(x1, y1, z1, x2, y2, z2)


