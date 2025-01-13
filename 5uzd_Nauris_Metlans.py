#Galvenā klase un tās metodes
class TransportLidzeklis:
    def __init__(self, razotajs, izlaiduma_gads, krasa, piedzina):
        self.razotajs = razotajs
        self.gads = izlaiduma_gads
        self.krasa = krasa
        self.piedzina = piedzina
    
    def parkrasot(self, krasa):
        if self.krasa == krasa:
            print(f"Transportlīdzeklis jau ir {krasa} krāsā!")
        else:
            print(f"Transportlīdzeklis pārkrāsots {krasa} krāsā!")
            self.krasa = krasa
    def mainit_piedzinu(self, piedzina):
        if self.piedzina == piedzina:
            print(f"Transportlīdzeklim jau ir {piedzina} piedziņa!")
        else:
            print(f"Transportlīdzekļa piedziņa mainīta uz {piedzina}!")
            self.piedzina = piedzina
    def info(self):
        print(f"Transportlīdzekļa ražotājs ir {self.razotajs}, tā izlaiduma gads ir {self.gads}, tas ir {self.krasa} krāsā un tam ir {self.piedzina} piedziņa!")

#Bērna klase TransportLidzeklis klasei un tās metodes         
class Masina(TransportLidzeklis):
    def __init__(self, razotajs, izlaiduma_gads, krasa, piedzina, durvju_skaits):
        super().__init__(razotajs, izlaiduma_gads, krasa, piedzina)
        self.durvju_skaits = durvju_skaits
        self.uzskaite = True
    def norakstit(self):
        if self.uzskaite == True:
            print(f"Automašīna {self.razotajs} norakstīta!")
            self.uzskaite = False
        else:
            print(f"Automašīna {self.razotajs} nav uzskaitē!")
    def info(self):
        if self.uzskaite:
            uzskaites_status = "uzskaitē"
        else:
            uzskaites_status = "norakstīta"
        print(f"Auto ražotājs ir {self.razotajs}, tā izlaiduma gads ir {self.gads}, tas ir {self.krasa} krāsā un tam ir {self.piedzina} piedziņa! Auto ir {self.durvju_skaits} durvis! Un tā ir {uzskaites_status}!")

ritenis = TransportLidzeklis("Ērempreiss", 1979, "zilā", "aizmugures")
#Izmantojam metodi pārkrāsot
ritenis.parkrasot("zaļā")
#Nomainam piedziņu ar metodi mainit_piedzinu
ritenis.mainit_piedzinu("priekšas")
#Izdrukājam informāciju par transportlīdzekli
ritenis.info()
#Mēģinam vēlreiz nomainīt piedziņu uz jau esošu
ritenis.mainit_piedzinu("priekšas")

auto = Masina("Audi", 1999, "pelēkā", "priekšas", 4)
#Izdrukājam informāciju par auto
auto.info()
#Norakstam auto ar metodi norakstit
auto.norakstit()
#Izdrukājam informāciju par auto
auto.info()
#Mēģinam vēlreiz norakstīt
auto.norakstit()
#Nomainam piedziņu ar vecāka klases metodi mainit_piedzinu
auto.mainit_piedzinu("pilnpiedziņas")
#Izdrukājam informāciju par auto
auto.info()
#Nomainam krāsu ar vecāka klases metodi parkrasot
auto.parkrasot("melna")
#Izdrukājam informāciju par auto
auto.info()