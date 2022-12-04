from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()
        ekan_siirto = self._ensimmainen_siirto()
        tokan_siirto = self._toinen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmainen_siirto()
            tokan_siirto = self._toinen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)
    
    def _ensimmainen_siirto(self):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        return ekan_siirto
    
    def _toinen_siirto(self, ensimmainen_siirto):
        return ensimmainen_siirto

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toinen_siirto(self, ekan_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toinen_siirto(self, ekan_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)
    
    def _toinen_siirto(self, ekan_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto

def luo_peli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    if tyyppi == 'b':
        return KPSTekoaly()
    if tyyppi == 'c':
        return KPSParempiTekoaly()
    return None