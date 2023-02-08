n = int(input("Enter the number of rows: "))   
for i in range(1, n+1):  
    for j in range(1, n-i+1):  
        print(end=" ")
    for j in range(1, 2*i):
        if i%2==1:
            if j%2==1:
                print('+',end='')
            else:
                print("*", end='')  
        else:
            if j%2==1:
                print('*',end='')
            else:
                print("+", end='')
    print()  
for i in range(n-1,0,-1):  
    for j in range(1, n-i+1):  
        print(end=" ")
    for j in range(1, 2*i):  
        if i%2==1:
            if j%2==1:
                print('+',end='')
            else:
                print("*", end='')  
        else:
            if j%2==1:
                print('*',end='')
            else:
                print("+", end='')  
    print()