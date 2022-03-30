def AmstrongNumber(x):
    sum = 0
    temp = x
    while temp > 0:
        r = temp % 10
        sum += r ** 3
        temp //= 10
    if x == sum:
        return True
    else:
        return False

def Div_8(x):
    if x%8 ==0:
        return True
    else:
        return False

def Smallest(x,y,z):
    if x<y and x<z:
        return x
    elif y<x and y<z:
        return y
    else:
        return z

def EvenorOdd(x):
    if x%2 == 0:
        return True
    else:
        return False

def PalindromeorNot(x):
    if x == x[::-1]:
        return True

    else:
        return False

if __name__ == "__main__":

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    amstrong = AmstrongNumber(a)
    print(amstrong)
    div_8 = Div_8(a)
    print(div_8)
    smallest = Smallest(a,b,c)
    print(smallest)
    evenorodd = EvenorOdd(a)
    print(evenorodd)
    palindrome = PalindromeorNot(a)
    print(palindrome)