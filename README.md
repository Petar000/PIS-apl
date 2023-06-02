# Sustav za upravljanje zaposlenicima

## Opis

Cilj aplikacije je upravljanje informacijama o zaposlenicima jedne firme. Ovo je backend aplikacija u kojoj je omogućeno kreiranje, pregledavanje, ažuriranje i brisanje podataka o zaposlenicima. Svaki zaposlenik ima svoj: ID, ime, prezime, pozicija i plaća. Korisnik može sortirati zaposlenike prema plaći od najveće prema najmanjoj. Također se mogu filtrirati zaposlenici prema zadanim kriterijima kako bi pronašli odgovarajuće ili odgovarajućeg zaposlenika. Iz toga vidimo da aplikacija ima funkcionalnosti za: stvoriti zaposlenike, pregledati zaposlenike, ažurirati zaposlenike, obrisati željene zaposlenike, filtrirati zaposlenike te sortirati zaposlenike prema plaći.

## Pokretanje

1. **Kloniranje repozitorija**

Kako biste klonirali ovaj repozitorij na svoje računalo, otvorite terminal ili neki drugi naredbeni redak, navigirajte do direktorija u kojem želite smjestiti projekt i izvršite sljedeću naredbu:

git clone https://github.com/Petar000/PIS-apl.git

2. **Instalacija Docker Desktop-a**

Ako nemate instaliran Docker Desktop, potrebno ga je instalirati putem linka: https://www.docker.com/products/docker-desktop/

3. **Izgradnja Docker image-a**

Nakon što ste klonirali repozitorij, otvorite terminal i navigirajte do direktorija projekta. Zatim izvršite sljedeću naredbu kako biste izgradili Docker image:

docker build -t pis-docker .

Na ovaj način ćete izraditi docker image s nazivom "pis-docker" koristeći Dockerfile koji se nalazi u direktoriju projekta.

4. **Pokretanje Docker kontenjera**

Nakon što ste uspješno izgradili Docker image, možete pokrenuti Docker kontejner slijedećom naredbom:

docker run -p 5000:5000 pis-docker

Ovo će pokrenuti Docker kontejner temeljen na prethodno izgrađenom Docker image-u i omogućiti pristup aplikaciji putem HTTP na portu 5000.

Nakon izvršavanja ovih koraka, aplikacija će biti pokrenuta unutar Docker kontejnera i možete pristupiti aplikaciji preko http://localhost:5000 .