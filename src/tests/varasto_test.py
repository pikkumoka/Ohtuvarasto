import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    #lisätyt testit
    def test_negatiivinen_lisäys_varastoon(self) :
        alkuperainen_saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, alkuperainen_saldo)

    def test_liikaa_tavaraa_varastoon(self) :
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_negatiivinen_maara(self) :
        alkuperainen_saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(self.varasto.saldo, alkuperainen_saldo)

    def test_ota_varastosta_liikaa(self) :
        alkuperainen_saldo = self.varasto.saldo

        self.assertAlmostEqual(self.varasto.ota_varastosta(11), alkuperainen_saldo)

    def test_uusi_varasto_neg_tilavuus(self) :
        mun_varasto = Varasto(-5)

        self.assertAlmostEqual(mun_varasto.tilavuus, 0)

    def test_uusi_varasto_neg_saldo(self) :
        mun_varasto = Varasto(10, -5)

        self.assertAlmostEqual(mun_varasto.saldo, 0)

    def test_varaston_tilanne(self) :
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")