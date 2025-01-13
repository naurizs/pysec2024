#Kods parāda sava izņēmuma veidošanu un visparējo izņēmumu izmantošanu, lai notestētu definēto, var ievadīt skaitli lielāku par 100

class lielaksparsimts(Exception):
    def __init__(self, kluda="Viens no skaitļiem ir lielāks par 100!!!"):
        self.message = kluda
        super().__init__(self.message)
        
try:
    a = int(input("Ievadiet skaitli mazāku par 100, kas būs dalāmais: "))
    b = int(input("Ievadiet skaitli mazāku par 100, kas būs dalītājs: "))
except ValueError:
    print(f"Kļūda: abiem jābūt skaitļiem!!!") 
    exit(1) 
except Exception as e:
    print(f"Kļūda: {e}")  

try:
    if (a>100 or b>100):
        raise lielaksparsimts
    else:
        print(a/b)
except lielaksparsimts as e:
    print(f"Kļūda: {e}")
except ZeroDivisionError:
    print(f"Kļūda: nevar dalīt ar nulli!!!")   
except NameError:
    print(f"Kļūda: abiem jābūt skaitļiem!!!") 
except Exception as e:
    print(f"Kļūda: {e}")  