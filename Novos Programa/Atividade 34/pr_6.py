lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for j in range(20):
    if primo(lista[j-1]):
        print(f"{lista[j-1]} é um número primo.")
    else:
        print(f"{lista[j-1]} não é um número primo.")