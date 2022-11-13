import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
  def setUp(self):
    self.kassa = Kassapaate()
    self.kortti = Maksukortti(1000)

  def test_luotu_kassa_on_olemassa(self):
    self.assertNotEqual(self.kassa, None)

  def test_luodussa_kassassa_tuhat_euroa(self):
    # määrä senteissä
    self.assertEqual(self.kassa.kassassa_rahaa, 100000)

  def test_luodussa_kassassa_nolla_myytya_edullista_lounasta(self):
    self.assertEqual(self.kassa.edulliset, 0)

  def test_luodussa_kassassa_nolla_myytya_maukasta_lounasta(self):
    self.assertEqual(self.kassa.maukkaat, 0)
  
  def test_edullinen_lounas_riittavalla_kateismaksulla_kerryttaa_kassaa(self):
    self.kassa.syo_edullisesti_kateisella(500)
    self.assertEqual(self.kassa.kassassa_rahaa, 100240)
  
  def test_edullinen_lounas_riittavalla_kateismaksulla_palauttaa_oikean_vaihtorahan(self):
    vaihtoraha = self.kassa.syo_edullisesti_kateisella(500)
    self.assertEqual(vaihtoraha, 260)
  
  def test_edullinen_lounas_riittavalla_kateismaksulla_kasvattaa_myytyja_edullisia_lounaita(self):
    self.kassa.syo_edullisesti_kateisella(500)
    self.assertEqual(self.kassa.edulliset, 1)

  def test_edullinen_lounas_riittamattomalla_kateismaksulla_ei_kerryta_kassaa(self):
    self.kassa.syo_edullisesti_kateisella(200)
    self.assertEqual(self.kassa.kassassa_rahaa, 100000)

  def test_edullinen_lounas_riittamattomalla_kateismaksulla_palauttaa_maksun(self):
    vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
    self.assertEqual(vaihtoraha, 200)

  def test_riittamaton_kateismaksu_edullisten_lounaiden_maara_ei_muutu(self):
    self.kassa.syo_edullisesti_kateisella(200)
    self.assertEqual(self.kassa.edulliset, 0)
  
  def test_maukas_lounas_riittavalla_kateismaksulla_kerryttaa_kassaa(self):
    self.kassa.syo_maukkaasti_kateisella(500)
    self.assertEqual(self.kassa.kassassa_rahaa, 100400)
  
  def test_maukas_lounas_riittavalla_kateismaksulla_palauttaa_oikean_vaihtorahan(self):
    vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
    self.assertEqual(vaihtoraha, 100)
  
  def test_maukas_lounas_riittavalla_kateismaksulla_kasvattaa_myytyja_maukkaita_lounaita(self):
    self.kassa.syo_maukkaasti_kateisella(500)
    self.assertEqual(self.kassa.maukkaat, 1)

  def test_maukas_lounas_riittamattomalla_kateismaksulla_ei_kerryta_kassaa(self):
    self.kassa.syo_maukkaasti_kateisella(200)
    self.assertEqual(self.kassa.kassassa_rahaa, 100000)

  def test_maukas_lounas_riittamattomalla_kateismaksulla_palauttaa_maksun(self):
    vaihtoraha = self.kassa.syo_maukkaasti_kateisella(200)
    self.assertEqual(vaihtoraha, 200)

  def test_riittamaton_kateismaksu_maukkaiden_lounaiden_maara_ei_muutu(self):
    self.kassa.syo_maukkaasti_kateisella(200)
    self.assertEqual(self.kassa.maukkaat, 0)

  def test_kortilta_veloitetaan_edullisen_lounaan_hinta_kun_kortin_saldo_riittaa(self):
    self.kassa.syo_edullisesti_kortilla(self.kortti)
    self.assertEqual(self.kortti.saldo, 760)
  
  def test_kassa_palauttaa_True_jos_maksukortin_saldo_riittaa_edulliseen_lounaaseen(self):
    tulos = self.kassa.syo_edullisesti_kortilla(self.kortti)
    self.assertEqual(tulos, True)

  def test_kortilla_maksettu_edullinen_lounas_kasvattaa_myytyjen_edullisten_lounaiden_maaraa(self):
    self.kassa.syo_edullisesti_kortilla(self.kortti)
    self.assertEqual(self.kassa.edulliset, 1)

  def test_kortin_saldo_ei_muutu_jos_maksukortin_saldo_ei_riita_edullisen_lounaan_maksuun(self):
    kortti = Maksukortti(100)
    self.kassa.syo_edullisesti_kortilla(kortti)
    self.assertEqual(kortti.saldo, 100)

  def test_myytyjen_edullisten_lounaiden_maara_ei_muutu_jos_maksukortin_saldo_ei_riita_edullisen_lounaan_maksuun(self):
    kortti = Maksukortti(100)
    self.kassa.syo_edullisesti_kortilla(kortti)
    self.assertEqual(self.kassa.edulliset, 0)

  def test_kassa_palauttaa_False_jos_maksukortin_saldo_ei_riita_edullisen_lounaan_maksuun(self):
    kortti = Maksukortti(100)
    tulos = self.kassa.syo_edullisesti_kortilla(kortti)
    self.assertEqual(tulos, False)

  def test_kortilta_veloitetaan_maukkaan_lounaan_hinta_kun_kortin_saldo_riittaa(self):
    self.kassa.syo_maukkaasti_kortilla(self.kortti)
    self.assertEqual(self.kortti.saldo, 600)
  
  def test_kassa_palauttaa_True_jos_maksukortin_saldo_riittaa_maukkaaseen_lounaaseen(self):
    tulos = self.kassa.syo_maukkaasti_kortilla(self.kortti)
    self.assertEqual(tulos, True)

  def test_kortilla_maksettu_maukas_lounas_kasvattaa_myytyjen_maukkaiden_lounaiden_maaraa(self):
    self.kassa.syo_maukkaasti_kortilla(self.kortti)
    self.assertEqual(self.kassa.maukkaat, 1)

  def test_kortin_saldo_ei_muutu_jos_maksukortin_saldo_ei_riita_maukkaan_lounaan_maksuun(self):
    kortti = Maksukortti(100)
    self.kassa.syo_maukkaasti_kortilla(kortti)
    self.assertEqual(kortti.saldo, 100)

  def test_myytyjen_maukkaiden_lounaiden_maara_ei_muutu_jos_maksukortin_saldo_ei_riita_maukkaan_lounaan_maksuun(self):
    kortti = Maksukortti(100)
    self.kassa.syo_maukkaasti_kortilla(kortti)
    self.assertEqual(self.kassa.maukkaat, 0)

  def test_kassa_palauttaa_False_jos_maksukortin_saldo_ei_riita_maukkaan_lounaan_maksuun(self):
    kortti = Maksukortti(100)
    tulos = self.kassa.syo_maukkaasti_kortilla(kortti)
    self.assertEqual(tulos, False)

  def test_kassan_rahamaara_ei_muutu_kortilla_maksaessa(self):
    self.kassa.syo_edullisesti_kortilla(self.kortti)
    self.kassa.syo_maukkaasti_kortilla(self.kortti)
    self.assertEqual(self.kassa.kassassa_rahaa, 100000)

  def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ladatulla_summalla(self):
    self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
    self.assertEqual(self.kortti.saldo, 2000)
  
  def test_kortille_rahaa_ladattaessa_kassassa_oleva_rahamaara_muuttuu_ladatulla_summalla(self):
    self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
    self.assertEqual(self.kassa.kassassa_rahaa, 101000)
  
  def test_kortille_rahaa_ladattavan_summan_tulee_olla_positiivinen(self):
    self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
    self.assertEqual(self.kortti.saldo, 1000)
    self.assertEqual(self.kassa.kassassa_rahaa, 100000)
