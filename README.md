# kyselma
	Kyselmä - kysele, vastaile ja tutki tuloksia

Tarkoitus on luoda sivu jossa voi luoda kysymyksiä ja kyselyitä, joita
täytetään anonyymillä nimimerkillä.

Käyttäjä luo ensin kyselyn ja antaa omat vastauksensa.

Kyselyn luonti:
- Käyttäjä kirjoittaa kysymyksen
- Käyttäjä valistee kysymykseen sopivat vastinparit
- Käyttäjä vastaa itse kysymykseensä
- Em 3 kohtaa toistetaan, kunnes käyttäjä valitsee valmis
- Tämän jälkeen käyttäjä1 siirretään tarkastelutilaan

Vastausvaihtoehdot on muunnettavissa luvuiksi, joita voi vertailla.

Esimerkkivastinpareja:
- kyllä vs ei
- samaa mieltä vs eri mieltä
- vaihtoehto1 vs vaihtoehto2

Kyselytila:
- Käyttäjä 2 saa käyttäjän 1 esittämät kysymykset vastattavakseen
- Vastattuaan kysymyksiin käyttäjä 2 siirretään tarkastelu tilaan

Tarkastelutila:
- Tilassa näkyy kutsulinkki ja koodi, jolla käyttäjä voi kutsua toisen
- Tilassa voi valita monta eri moodia:
	1. Kaikkien vastausten kekiarvo
	2. Eniten omia vastauksia mukaileva käyttäjä
	3. Vähiten omia vastauksia mukaileva käyttäjä
	4. Etsi käyttäjä vertailtavaksi
- Kaikissa moodeissa vertaillaan vastauksia/keskiarvoa omiin
- Jokainen moodi näyttää myös yhtenäisyysprosentin

Yhtenäisyysprosentti:
- Tismalleen samat vastaukset antaa 100%
- Tismalleen eri ääripäiden vastaukset antaa 0%
- Jos vastausten välinen etäisyys koko skaalalla on 10% niin se antaa 90%
- Eli siis 1-abs(vast_a-vast_b)/(max-min)
- Kyselyn yhtenäisyysprosentti on keskiarvo kaikkien kysymysten prosenteista


Moderointitila:
- poista kysely kutsukoodilla
- esti kysely hakusanalla positettavasksi


Kysymykset, kyselyt, vastaukset tallennetaan asianmukaisiin tauluihin.


Ominaisuuksia joiden tekemistä voi harkita:
- Jokaisella kyselyllä on elinikä jonka jälkeen ne siivotaan.
- Kysymyksiin voi liittää kuvia
