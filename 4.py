# Iterativ funksiya
def fac_iterativ(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return result
        
n = 5       
print(f"Iterativ: {fac_iterativ(n)}")
# Recursive funksiya
def func(a):
    if a == 1:
        return 1
    return a + func(a-1)
s = func(3)
print("Recursive: ", s)

# lambda - anonimm funksiya
fun = lambda a,b : a*b
print("Lambda: ", fun(3,5))