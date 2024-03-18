def faktorial(n):
    for i in range(n,0,-1):
        tot=1
        for j in range(i,0,-1):  
            tot=tot*j
        print (tot,end=" ")
        for k in range(i,0,-1):
            print(k," ",end="")
        print()

n=int(input("input n:"))
faktorial(n)