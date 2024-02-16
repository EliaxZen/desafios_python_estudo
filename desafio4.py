def primo(n):
    if n <= 2: # 1 e 2 são primos
        return True
    for div in range(2, n):
        if n % div == 0:
            return False
    return True

for n in [1, 5, 10, 13, 15, 17]:
    print(n, 'é número primo?', primo(n))