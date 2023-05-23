def check_prime(n):
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
    return is_prime

count = 0
for n in range(1, 201):
    if check_prime(n):
        count += 1
        print(n, end="  ")

print('\nTotal prime number from 1 to 200 is', count)