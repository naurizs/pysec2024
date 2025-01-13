#----------------------------------------------------------------------------List piemērs------------------------------------------------------------------------------------------------------------------------------------
#Izveidojam datu tip list ar python kursa uzdevumiem
python_uzdevumi = ["1. Multiple compilers", "2. Virtual environments", "5. Classes", "3. Data types", "6. Exceptions", "7. Modules", "9. Directory travel", "11. Signal handler", "12. File downloader", "13. FTP parser", "14. TCP SYN scanner", "15. Password cracker"]

#Izdrukājam list
print(python_uzdevumi)

#Izpakojam bez cikla un izdrukājam katru savā rindā
print("Python uzdevumi: \n", *python_uzdevumi,sep='\n')

#Pievienojam iztrūkstošo uzdevumu pa vienam
python_uzdevumi.append("4. Loops")

#Pievienojam pa vairākiem
python_uzdevumi.extend(["8. Read log file", "10. Threads"])

#Cenšamies sakārtot listi
python_uzdevumi.sort()

#Izpakojam bez cikla un izdrukājam katru savā rindā
print("Python uzdevumi sakārtoti: \n", *python_uzdevumi,sep='\n')

python_uzdevumi.remove("15. Password cracker")

#Izpakojam bez cikla un izdrukājam katru savā rindā
print("Python uzdevumi: \n", *python_uzdevumi,sep='\n')

#Izdukājam kopējo uzdevumu skaitu
print("Kopā uzdevumi: ", len(python_uzdevumi))

#----------------------------------------------------------------------------Dictionary piemērs------------------------------------------------------------------------------------------------------------------------------------
#Izveidojam datu tipu dictionary ar dažādām konstantēm
konstantes = {'pi':'3.14', 'gaismas ātrums':'299792458 m/s', 'gravitācija':'9.8m/s'}

#Izdrukājam vārdnīcu
print("\n", konstantes)

#Nomainam pi
konstantes['pi'] = '3.14159'

#Izdrukājam jauno pi
print("\n Pi vērtība ir: ", konstantes['pi'])

konstantes['dienas nedēļā'] = 7

#Izdrukājam vārdnīcu
print("\n", konstantes)

#Izdzēšam elementu
del konstantes['dienas nedēļā']

#Izdrukājam vārdnīcu
print("\n", konstantes)

#----------------------------------------------------------------------------Set piemērs------------------------------------------------------------------------------------------------------------------------------------
#Izveidojam datu tip set ar personu vārdiem
vardi = {"Jānis", "Pēteris", "Kristaps", "Ilze", "Zane", "Kristīne"}

#Izdrukājam
print("\n", vardi)

#Cenšamies pievienot vēl vienu jau esošu vārdu
vardi.add("Kristīne")

#Izpakojam un izdrukājam, redzam, ka nav pievienots, jo tāds jau Setā eksistē un Set sastāv no unikālām vērtībām
print("\n", *vardi, sep='\n')

#Cenšamies pievienot vēl vienu neesošu vārdu
vardi.add("Paulīne")

#Izpakojam un izdrukājam
print("\n", *vardi,'\n', sep='\n')

#----------------------------------------------------------------------------Tuple piemērs--------------------------------------------------------------------------------------------------------------------------------------
#Izveidojam datu tipu tuple ar dažādām konstantēm
konstantes_tuple = ("pi", 3.14, "gaismas_atrums", '299792458 m/s', 'gravitācija', '9.8m/s')

#Izpakojam tuple mainīgajos
konst1,vert1,konst2,vert2,konst3,vert3 =  konstantes_tuple

#Izdrukājam mainīgos
print(konst1,'=',vert1,'\n')
print(konst2,'=',vert2,'\n')
print(konst3,'=',vert3,'\n')

