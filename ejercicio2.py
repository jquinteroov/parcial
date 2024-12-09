print("ingrese el numero entero positivo")
n = int(input())
while(n>1):
    if n>1:
        break
    
    else:
    
        while (n%2==0):
            n= n/2
            print(n)
        while (n%2>0):
            n=(n*3)+1
            print(n)