from flask import Flask, jsonify, request
from pony.orm import db_session, desc, select
from baza import Zaposlenici, db
from collections import OrderedDict

app = Flask(__name__)

@app.route('/zaposlenik', methods=['GET'])
@db_session
def dohvati_zaposlenike():
    zaposlenici = Zaposlenici.select()[:]
    zaposlenici_json = []
    for zaposlenik in zaposlenici:
        zaposlenik_dict = OrderedDict([
            ('id', zaposlenik.id),
            ('ime', zaposlenik.ime),
            ('prezime', zaposlenik.prezime),
            ('pozicija', zaposlenik.pozicija),
            ('placa', zaposlenik.placa)
        ])
        zaposlenici_json.append(zaposlenik_dict)
    return jsonify(zaposlenici_json)

@app.route('/zaposlenik', methods=['POST'])
@db_session
def dodaj_zaposlenika():
    podaci = request.get_json()
    ime = podaci['ime']
    prezime = podaci['prezime']
    pozicija = podaci['pozicija']
    placa = podaci['placa']
    
    zaposlenik = Zaposlenici(ime=ime, prezime=prezime, pozicija=pozicija, placa=placa)
    db.commit()
    
    return jsonify({'message': 'Zaposlenik je uspješno dodan.'})

@app.route('/zaposlenik/poplaci', methods=['GET'])
@db_session
def dohvati_zaposlenike_sortirano():
    zaposlenici = Zaposlenici.select().order_by(desc(Zaposlenici.placa))[:]
    zaposlenici_json = []
    for zaposlenik in zaposlenici:
        zaposlenik_dict = OrderedDict([
            ('id', zaposlenik.id),
            ('ime', zaposlenik.ime),
            ('prezime', zaposlenik.prezime),
            ('pozicija', zaposlenik.pozicija),
            ('placa', zaposlenik.placa)
        ])
        zaposlenici_json.append(zaposlenik_dict)
    return jsonify(zaposlenici_json)

@app.route('/zaposlenik/<id>', methods=['DELETE'])
@db_session
def obrisi_zaposlenika(id):
    zaposlenik = Zaposlenici.get(id=id)
    if not zaposlenik:
        return jsonify({'message': 'Nema zaposlenika s navedenim prezimenom.'})
    
    zaposlenik.delete()
    db.commit()

    return jsonify({'message': 'Zaposlenik je uspješno obrisan.'})


@app.route('/zaposlenik/<id>', methods=['PUT'])
@db_session
def azuriraj_zaposlenika(id):
    zaposlenik = Zaposlenici.get(id=id)
    if not zaposlenik:
        return jsonify({'message': 'Nema zaposlenika s navedenim prezimenom.'})
    
    novi_podaci = request.get_json()
    if 'ime' in novi_podaci:
        zaposlenik.ime = novi_podaci['ime']
    if 'prezime' in novi_podaci:
        zaposlenik.prezime = novi_podaci['prezime']
    if 'pozicija' in novi_podaci:
        zaposlenik.pozicija = novi_podaci['pozicija']
    if 'placa' in novi_podaci:
        zaposlenik.placa = novi_podaci['placa']
    
    db.commit()

    return jsonify({'message': 'Zaposlenik je uspješno ažuriran.'})

@app.route('/zaposlenici', methods=['GET'])
@db_session
def filtriraj_zaposlenike():
    # Dohvaćanje parametara za filtriranje iz URL query stringa
    id = request.args.get('id')
    ime = request.args.get('ime')
    prezime = request.args.get('prezime')
    pozicija = request.args.get('pozicija')
    placa = request.args.get('placa')

    # Filtriranje zaposlenika na temelju zadanih uvjeta
    filteri = {'id': id, 'ime': ime, 'prezime': prezime, 'pozicija': pozicija, 'placa': placa}

    zaposlenici = Zaposlenici.select()
    for k, v in filteri.items():
        if v is not None:
            zaposlenici = zaposlenici.filter(**{k: v})

    rezultati = []
    for zaposlenik in zaposlenici:
        rezultati.append({
            'id': zaposlenik.id,
            'ime': zaposlenik.ime,
            'prezime': zaposlenik.prezime,
            'pozicija': zaposlenik.pozicija,
            'placa': zaposlenik.placa
        })

    if not rezultati:
        return jsonify({'message': 'Nema zaposlenika koji zadovoljavaju zadane uvjete.'})

    return jsonify(rezultati)

if __name__ == '__main__':
    app.run()