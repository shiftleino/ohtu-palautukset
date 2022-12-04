class Tuomari:
    """
    Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
    """
    def __init__(self):
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        if self._tasapeli(ekan_siirto, tokan_siirto):
            self.tasapelit += 1
        elif self._eka_voittaa(ekan_siirto, tokan_siirto):
            self.ekan_pisteet += 1
        else:
            self.tokan_pisteet += 1

    def __str__(self):
        return f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\nTasapelit: {self.tasapelit}"

    def _tasapeli(self, ekan_siirto, tokan_siirto):
        return ekan_siirto == tokan_siirto

    def _eka_voittaa(self, ekan_siirto, tokan_siirto):
        if ekan_siirto == "k" and tokan_siirto == "s":
            return True
        elif ekan_siirto == "s" and tokan_siirto == "p":
            return True
        elif ekan_siirto == "p" and tokan_siirto == "k":
            return True
        return False