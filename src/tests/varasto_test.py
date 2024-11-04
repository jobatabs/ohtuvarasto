"""Unit tests for Varasto
"""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Unit testing class for Varasto
    """
    def setUp(self):
        """Setting up the tests
        """
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Does the constructor create an empty storage
        """
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Does the new storage have correct space
        """
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_negatiivinen_tilavuus(self):
        """Does the constructor handle negative storage
        """
        neg = Varasto(-10)

        self.assertAlmostEqual(neg.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        """Does the constructor handle negative saldo
        """
        neg_saldo = Varasto(10, -10)

        self.assertAlmostEqual(neg_saldo.saldo, 0)

    def test_lisaa_negatiivinen(self):
        """Add negative
        """
        self.varasto.lisaa_varastoon(-10)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        """Does adding add saldo
        """
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_liian_suuri_lisays(self):
        """Adding too much
        """
        self.varasto.lisaa_varastoon(200)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_negatiivinen(self):
        """Taking negative amount
        """
        reply = self.varasto.ota_varastosta(-10)

        self.assertAlmostEqual(reply, 0)

    def test_ota_liikaa(self):
        """Taking too much
        """
        reply = self.varasto.ota_varastosta(200)

        self.assertAlmostEqual(reply, 0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Does adding remove available space
        """
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Does taking return correct amount
        """
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Does taking add space
        """
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_string(self):
        """Test string representation
        """
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
