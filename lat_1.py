def cek_prima(n):
    if n<2:
        return False
    elif n==2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
# prima terdekat
def nearest_prime(n):
    angka=n-1
    for i in range(angka,0,-1):
        if cek_prima(i)==True:
            return i
        
n=int(input("masukan n:"))
cek_prima(n)
nearest_prime(n)
print(f"Bilangan prima terdekat < {n} adalah {nearest_prime(n)}")
