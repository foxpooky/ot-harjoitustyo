import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
  def setUp(self):
    self.maksukortti = Maksukortti(1000)

  def test_luotu_kortti_on_olemassa(self):
    self.assertNotEqual(self.maksukortti, None)

  def test_asettaa_saldon_oikein(self):
    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

  def test_arvon_lataaminen_kasvattaa_saldoa_oikein(self):
    self.maksukortti.lataa_rahaa(1000)
    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

  def test_rahan_ottaminen_pienentaa_saldoa_jos_rahaa_on_tarpeeksi(self):
    self.maksukortti.ota_rahaa(500)
    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

  def test_rahan_ottaminen_ei_vaikuta_saldoon_jos_rahaa_ei_ole_tarpeeksi(self):
    self.maksukortti.ota_rahaa(1100)
    self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
  
  def test_rahan_ottaminen_palauttaa_True_kun_rahat_riittavasti(self):
    self.assertEqual(self.maksukortti.ota_rahaa(200), True)
  
  def test_rahan_ottaminen_palauttaa_False_kun_rahat_eivat_riita(self):
    self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
