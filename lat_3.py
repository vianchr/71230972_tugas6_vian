tinggi=int(input("masukan tinggi:"))
lebar=int(input("masukan lebar:"))
angka=0
for i in range(tinggi):
    for j in range(1,lebar+1):
        angka+=1
        print(angka,end=" ")
    print ()
    