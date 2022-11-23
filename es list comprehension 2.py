def isPrimo(x):
    
    for i in range(2, int(x**0.5)+1):

        if(x%i==0):

            return False

    return True

n = 100

l=[i for i in range(1, n+1)if isPrimo(i)]

print(l)