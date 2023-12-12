class Animal:
    def __init__(self, name, nature, size, jum_kaki):
        self.name = name
        self.nature = nature
        self.size = size
        self.jum_kaki = jum_kaki

    def display_info(self):
        print(f"Name: {self.name}, Nature: {self.nature}, Size: {self.size}, Legs: {self.jum_kaki}")


class Mamalia(Animal):
    def __init__(self, name, nature, size, jum_kaki, bisa_jalan, jenis_mamalia):
        super().__init__(name, nature, size, jum_kaki)
        self.bisa_jalan = bisa_jalan
        self.jenis_mamalia = jenis_mamalia

    def display_info(self):
        super().display_info()
        print(f"Bisa Jalan: {self.bisa_jalan}, Jenis Mamalia: {self.jenis_mamalia}")


class Aves(Animal):
    def __init__(self, name, nature, size, jum_kaki, bisa_terbang, jenis_aves):
        super().__init__(name, nature, size, jum_kaki)
        self.bisa_terbang = bisa_terbang
        self.jenis_aves = jenis_aves

    def display_info(self):
        super().display_info()
        print(f"Bisa Terbang: {self.bisa_terbang}, Jenis Aves: {self.jenis_aves}")


class Ayam(Aves):
    def __init__(self, name, nature, size, jum_kaki, bisa_terbang, jenis_aves, jenis_ayam, bisa_diadu):
        super().__init__(name, nature, size, jum_kaki, bisa_terbang, jenis_aves)
        self.jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu

    def display_info(self):
        super().display_info()
        print(f"Jenis Ayam: {self.jenis_ayam}, Bisa Diadu: {self.bisa_diadu}")


class Burung(Aves):
    def __init__(self, name, nature, size, jum_kaki, bisa_terbang, jenis_aves):
        super().__init__(name, nature, size, jum_kaki, bisa_terbang, jenis_aves)


class Merpati(Burung):
    def __init__(self, name, nature, size, jum_kaki, bisa_terbang, jenis_aves):
        super().__init__(name, nature, size, jum_kaki, bisa_terbang, jenis_aves)


# Contoh Penggunaan
singa = Mamalia("Singa", "Carnivore", "Large", 4, True, "Mamalia")
kuda = Mamalia("Kuda", "Herbivore", "Large", 4, True, "Mamalia")
ayam = Ayam("Ayam", "Omnivore", "Medium", 2, True, "Aves", "Ayam Kampung", True)
merpati = Merpati("Merpati", "Herbivore", "Small", 2, True, "Aves")

singa.display_info()
kuda.display_info()
ayam.display_info()
merpati.display_info()
