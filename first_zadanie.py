import hashlib
#1
"""
name = input()
#name += str()
#name = name.encode()
#value_hash = hashlib.sha256(name).hexdigest()
#print(value_hash)

#2
count_non = 0
count = 100
while count != 1000:
    name_2 = name+ str(count)
    name_2 = name_2.encode()
    value_hash = hashlib.sha256(name_2).hexdigest()
    if value_hash[0:2] == "00":
        print(value_hash)
        print(count)
        count_non += 1
    count += 1

print(count_non)
"""
#4
def fanc(tx1, tx2):
    tx12 = (tx1+tx2).encode()
    tx12 = hashlib.sha256(tx12).hexdigest()
    return tx12

mass = ['tx1', 'tx2' , 'tx3', 'tx4', 'tx1', 'tx2' , 'tx3', 'tx4']
mass2 = []
for i in range(0, len(mass)):
    mass[i] = mass[i].encode()
    mass[i] = hashlib.sha256(mass[i]).hexdigest()
count = 0
count_end = len(mass)
while len(mass) != 1:

    gg = fanc(mass[count], mass[count + 1])
    count += 2
    mass2.append(gg)
    if(count == count_end):
        print(mass)
        mass.clear()
        for i in range(0, len(mass2)):
            mass.append(mass2[i])
        mass2.clear()
        count = 0
        count_end = len(mass)
print(mass[0])



"""
for i in range(0, len(mass)):
    mass[i] = mass[i].encode()
    mass[i] = hashlib.sha256(mass[i]).hexdigest()
for i in range(0,len(mass),2):
    mass_tw = fanc(mass[i],mass[i+1])
    mass2.append(mass_tw)
else:
    for i in range(0, len(mass2),2):
        mass_tw = fanc(mass2[i], mass2[i + 1])
        mass3.append(mass_tw)

for i in range(0, len(mass)/2):
    mass2_tw = []
    mass2.append((mass2_tw))
    for j in range(0, len(mass2[i])):


print(mass)
print(mass2)
print(mass3)
"""





