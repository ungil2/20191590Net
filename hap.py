n = int(input('Number: '))
res = ''

while n != 0:
    m = n % 2
    res = str(m) + res
    n = n // 2

print(res)