"""Defines class Varasto

Returns:
    Varasto: Varasto object
"""

class Varasto:
    """Modeles a storage area
    """
    def __init__(self, tilavuus, alku_saldo=0):
        """Constructor for Varasto

        Args:
            tilavuus (float): How large the storage is
            alku_saldo (float, optional): Beginning saldo \
            for the storage. Defaults to 0.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea.
    # Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        """How much space is left

        Returns:
            float: How much space is left
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Add to the storage

        Args:
            maara (float): How much to add
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Remove from storage

        Args:
            maara (float): How much to remove

        Returns:
            float: How much was removed
        """
        kaikki_mita_voidaan = maara
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
        else:
            self.saldo = self.saldo - maara

        return kaikki_mita_voidaan

    def __str__(self):
        """String representation of the storage

        Returns:
            str: How much saldo and space left
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
