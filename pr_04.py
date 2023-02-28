# WAP to display a/b where a and b are an integer. If b=0 display infinity
# by handling the zeroDivisonError.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

try:
    print(a/b)
    
except:
    print("infinity...")
