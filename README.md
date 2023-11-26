# kyselma
	Kyselmä - kysele, vastaile ja tutki tuloksia

TO GET IT RUNNING:
	
Install postgresql for local user & get it running (as in course material)
- $ wget https://github.com/hy-tsoha/local-pg/raw/master/pg-install.sh
- $ bash pg-install.sh
- $ postrgres &

Install poetry if nessesary. (refer your distro)
- $ pip install --user poetry
- $ pipx install poetry

Clone the source & install poetry dependencies
- $ git clone https://github.com/triionhe/kyselma.git
- $ cd kyselma
- $ export PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring (Just in case..)
- $ poetry install --no-root

Get database ready
- $ psql < SCHEMA.sql (BE CAREFUL! This drops some tables.)
	
Start the app in poetry virtual environment
- $ SQLALCHEMY_DATABASE_URI="postgresql:///$USER" SECRET_KEY=29347884 poetry run flask run

Surf to the webpage and start two sessions for better testing
- $ firefox http://localhost:5000/ http://127.0.0.1:5000/

There is ready made kyselmä named 'kysdemo' for testing.



DONE:
- Vastausten anto
- Vastausten tarkistelu
- Kyselyn luomisen näyttö
- Kyselyn lukitseminen vastattavaksi
- Kysymyksen näyttö
- Ulkoasu
- Voi lisätä kyselyn
- Kysymyksen mukana lisätään vastaus
- Kysymyksen lisäys
- Vastaustaulu
- Kysymystaulu
- Kyselytaulu
- Tietokantayhteys
- Nimierkkitaulu
- Nimimerkin käyttöönotto ja tarkistus
- Virheviestien kuljetus
- Nettisivurunko

TODO:
- Moderointi
- Parempi ulkoasu
- Vastauksen ja luomisen aloittamisen yksinkertaistaminen
- Tietoturvaseikat?
- Eniten ja vähiten yhdenmukaiset vastaajat
...

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

Ikonit (CC) pixellove:
https://www.svgrepo.com/collection/pixellove-bordered-vectors/
