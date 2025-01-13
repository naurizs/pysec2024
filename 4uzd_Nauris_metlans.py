skaitli1 = [2, 4, 6, 8, 10, 12, 14]
skaitli2 = [2, 4, 6, 8, 11, 10, 12, 14]

#Meklē pirmo nepāra skaitli sarakstā ar for ciklu, ja sarakstā nav nepāra skaitļu, tad izdrukā, ka nepāra skaitļu nav
for i in skaitli1:
    if i % 2 !=0:
        print("Pirmais nepāra skaitlis šajā sarakstā ir: ", i)
        break
else:
    print("Šajā sarakstā nepāra skaitļu nav!")
#Meklē pirmo nepāra skaitli sarakstā ar for ciklu, ja sarakstā nav nepāra skaitļu, tad izdrukā, ka nepāra skaitļu nav
for i in skaitli2:
    if i % 2 !=0:
        print("Pirmais nepāra skaitlis šajā sarakstā ir: ", i)
        break
else:
    print("Šajā sarakstā nepāra skaitļu nav!")	
    
#Meklē pirmo nepāra skaitli sarakstā ar while ciklu, ja sarakstā nav nepāra skaitļu, tad izdrukā, ka nepāra skaitļu nav
i = 0 
while i < len(skaitli1):
    if skaitli1[i] % 2 !=0:
        print("Pirmais nepāra skaitlis šajā sarakstā ir: ", skaitli1[i])
        break
    i += 1
else:
    print("Šajā sarakstā nepāra skaitļu nav!")	
#Meklē pirmo nepāra skaitli sarakstā ar while ciklu, ja sarakstā nav nepāra skaitļu, tad izdrukā, ka nepāra skaitļu nav
i = 0 
while i < len(skaitli2):
    if skaitli2[i] % 2 !=0:
        print("Pirmais nepāra skaitlis šajā sarakstā ir: ", skaitli2[i])
        break
    i += 1
else:
    print("Šajā sarakstā nepāra skaitļu nav!")	
#Meklē pirmo nepāra skaitli sarakstā ar for in range ciklu, ja sarakstā nav nepāra skaitļu, tad izdrukā, ka nepāra skaitļu nav
for i in range(len(skaitli1)):
    if skaitli1[i] % 2 !=0:
        print("Pirmais nepāra skaitlis šajā sarakstā ir: ", skaitli1[i])
        break
else:
    print("Šajā sarakstā nepāra skaitļu nav!")
#Meklē pirmo nepāra skaitli sarakstā ar for in range ciklu, ja sarakstā nav nepāra skaitļu, tad izdrukā, ka nepāra skaitļu nav
for i in range(len(skaitli2)):
    if skaitli2[i] % 2 !=0:
        print("Pirmais nepāra skaitlis šajā sarakstā ir: ", skaitli2[i])
        break
else:
    print("Šajā sarakstā nepāra skaitļu nav!")