import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto2 = Varasto(-1, -1)
        self.varasto3 = Varasto(5, 10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_konstruktori_tayttaa_varaston(self):
        self.assertAlmostEqual(self.varasto3.saldo, self.varasto3.tilavuus)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)
        self.assertAlmostEqual(self.varasto3.tilavuus, 5)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_liian_suuri_lisaus_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu() + 1)

        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        alkutila = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(alkutila, self.varasto.saldo)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_liian_suuri_ottaminen_tyhjentaa_varaston(self):
        alkusaldo = self.varasto3.saldo
        kaikki_mita_voidaan = self.varasto3.ota_varastosta(10)

        self.assertAlmostEqual(alkusaldo, kaikki_mita_voidaan)
        self.assertAlmostEqual(self.varasto3.saldo, 0)

    def test_negatiivinen_ottaminen_ei_tee_mitaan(self):
        alkutila = self.varasto.saldo
        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(alkutila, self.varasto.saldo)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varaston_tila_tulostuu_oikein(self):
        saldo = str(self.varasto3.saldo)
        paljonko_mahtuu = str(self.varasto3.paljonko_mahtuu())

        self.assertIn(saldo, str(self.varasto3))
        self.assertIn(paljonko_mahtuu, str(self.varasto3))