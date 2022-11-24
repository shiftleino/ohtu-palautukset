from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._sisalto = []

    def tavaroita_korissa(self):
        return sum([ostos.lukumaara() for ostos in self._sisalto])

    def hinta(self):
        return sum([ostos.hinta() for ostos in self._sisalto])

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._sisalto:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return

        ostos = Ostos(lisattava)
        self._sisalto.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self._sisalto:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                
            if ostos.lukumaara() == 0:
                self._sisalto.remove(ostos)

    def tyhjenna(self):
        self._sisalto = []

    def ostokset(self):
        return self._sisalto