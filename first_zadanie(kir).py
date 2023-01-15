import hashlib

str='Kirill'.encode()
i = 0
j = 0

def hash_tree(first, second):
    first = hashlib.sha256(first.encode()).hexdigest()
    second = hashlib.sha256(second.encode()).hexdigest()
    str = first + second
    return str



for i in range(100, 1000):
    str=f"Kirill{i}"
    hash = hashlib.sha256(str.encode()).hexdigest()
    if hash[:2] == "00":
        j += 1
    i += 1


mas = ['tx1', 'tx2', 'tx3', 'tx4']

count = len(mas)
while (count > 0):
    for i in range(0, count, 2):
        mas[i//2] = hash_tree(mas[i], mas[i + 1])
    count = count//2
    print(mas)
print(mas[0])
