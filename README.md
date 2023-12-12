# kyselma
	Kyselmä - kysele, vastaile ja tutki tuloksia

## TO GET IT RUNNING:

#### Install postgresql for local user & get it running [as in course material](https://hy-tsoha.github.io/materiaali/osa-2/)
- `wget https://github.com/hy-tsoha/local-pg/raw/master/pg-install.sh`
- `bash pg-install.sh`
- `postrgres &`

#### Clone the source
- `git clone https://github.com/triionhe/kyselma`
- `cd kyselma`

#### Get database ready
- `psql < SCHEMA.sql` (BE CAREFUL! This drops some tables.)
	
#### Either use (1) poetry or (2) venv to handle dependencies and run the app

(1) Install poetry if nessesary. (refer your distro)
- `pip install --user poetry`
- `pipx install poetry`

(1) Install dependencies
- `PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring poetry install --no-root`

(1) Start the app in poetry virtual environment
- `poetry run flask run`

(2) Activate venv environment
- `python3 -m venv venv`
- `source venv/bin/activate`

(2) Install dependencies with pip
- `pip install -r ./requirements.txt`

(2) Start the app
- `flask run`

#### Surf to the webpage 
- `firefox http://127.0.0.1:5000/`

There is ready made kyselmä named 'kysdemo' for testing.





## DONE:
- Nimimerkin resetointi nimimerkistä 5s painamalla
- Tyhjien kysymysten laatiminen ei onnistu
- Linkin kyselyyn voi kopioida leikepöydälle
- Tietoturvaseikat: CSRF suojaus
- Eniten ja vähiten yhdenmukaiset vastaajat
- Parempi ulkoasu
- Vastauksen ja luomisen aloittamisen yksinkertaistaminen
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

## TODO:
- Moderointi

...

## Kuvaus:

Tarkoitus on luoda sivu jossa voi luoda kysymyksiä ja kyselyitä, joita
täytetään anonyymillä nimimerkillä.

Käyttäjä luo ensin kyselyn ja antaa omat vastauksensa.

### Käyttäjän luonti:
- Tässä ohjelmassa ei ole käyttäjiä vaan ainoastaan nimimerkkejä
- Nimimerkki on sessiokohtainen ja enempi vähempi pysyvä

### Kyselyn luonti:
- Käyttäjä kirjoittaa kysymyksen
- Käyttäjä valistee kysymykseen sopivat vastinparit
- Käyttäjä vastaa itse kysymykseensä
- Em 3 kohtaa toistetaan, kunnes käyttäjä valitsee valmis
- Tämän jälkeen käyttäjä1 siirretään tarkastelutilaan

Vastausvaihtoehdot on muunnettavissa luvuiksi, joita voi vertailla.

### Esimerkkivastinpareja:
- kyllä vs ei
- samaa mieltä vs eri mieltä
- vaihtoehto1 vs vaihtoehto2

### Kyselytila:
- Käyttäjä 2 saa käyttäjän 1 esittämät kysymykset vastattavakseen
- Vastattuaan kysymyksiin käyttäjä 2 siirretään tarkastelu tilaan

### Tarkastelutila:
- Tilassa näkyy kutsulinkki ja koodi, jolla käyttäjä voi kutsua toisen
- Tilassa voi valita monta eri moodia:
	1. Eniten omia vastauksia mukaileva käyttäjä
	2. Vähiten omia vastauksia mukaileva käyttäjä
	3. Etsi käyttäjä vertailtavaksi
- Kaikissa moodeissa vertaillaan vastauksia/keskiarvoa omiin
- Jokainen moodi näyttää myös yhtenäisyysprosentin

### Yhtenäisyysprosentti:
- Tismalleen samat vastaukset antaa 100%
- Tismalleen eri ääripäiden vastaukset antaa 0%
- Jos vastausten välinen etäisyys koko skaalalla on 10% niin se antaa 90%
- Eli siis 1-abs(vast_a-vast_b)/(max-min)
- Kyselyn yhtenäisyysprosentti on keskiarvo kaikkien kysymysten prosenteista


### Moderointitila:
- poista kysely kutsukoodilla
- esti kysely hakusanalla positettavasksi


### Kysymykset, kyselyt, vastaukset tallennetaan asianmukaisiin tauluihin.


### Ominaisuuksia joiden tekemistä voi harkita:
- Jokaisella kyselyllä on elinikä jonka jälkeen ne siivotaan.
- Kysymyksiin voi liittää kuvia

Ikonit (CC) pixellove:
https://www.svgrepo.com/collection/pixellove-bordered-vectors/
