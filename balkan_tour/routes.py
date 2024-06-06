from flask import render_template, request, redirect, url_for
from main import Session
from models import Tour, Client
from . import app  #čia importuojuos app objektą iš __init__.py failo, nors galiu ir čia turbūt įsikelt

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add_tour', methods=['GET', 'POST'])
def add_tour():
    session = Session()  # atidarau seimo sesiją
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        description = request.form['description']

        new_tour = Tour(name=name, location=location, description=description)
        session.add(new_tour)
        session.commit()

        return redirect(url_for('add_tour'))

    # Gaunu visus turus iš duomenų bazės





    tours = session.query(Tour).all()

    session.close()

    return render_template('add_tour.html', tours=tours)


@app.route('/tours')
def tours():
    return render_template('tours.html')

@app.route('/contacts', methods=['GET', 'POST']) #šituos reiks pasidaryti kai į normalų serverį įkelsiu
def contacts():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        question = request.form['question']

        return redirect(url_for('index'))
    return render_template('contacts.html')

@app.route('/add_client', methods=['GET', 'POST'])#get gauname duomenis is serverio, post siunciame duomenis i serveri
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        tour_id = request.form['tour'] #cia eina rekvestas su post metodu, susirenku duomenis is inputu

        session = Session()
        tour = session.query(Tour).get(tour_id)
        tour_name = tour.name #cia susijungiu su duombaze ir priskiriu klientui tura

        new_client = Client(name=name, surname=surname, email=email, tour_id=tour_id, tour_name=tour_name)
        session.add(new_client)
        session.commit()
        session.close() #kliento duomenys nukeliauja i duombaze ir sesija uzsidaro

        return redirect(url_for('add_tour')) #cia kad manes neismestu is puslapio


@app.route('/tour_details/<int:tour_id>')
def tour_details(tour_id):
    session = Session()
    tour = session.query(Tour).get(tour_id) #u=klausa kad gau2iau tura pagal nurodyt1 ID
    clients = session.query(Client).filter_by(tour_id=tour_id).all() #vel uzklausa kad gauciau visus klientus priristus prie sito turo
    session.close()
    return render_template('tour_details.html', tour=tour, clients=clients) #pateikiami html turas ir klienaikaip kintamieji

@app.route('/delete_client/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    session = Session()
    client = session.query(Client).get(client_id) #iskvieciame duombazej klienta pagal id
    session.delete(client) #SQAlcemy metdas istrina duomenis
    session.commit()
    session.close()
    return redirect(url_for('clients'))#pasilieku clinets puslapyje

@app.route('/client_list') #sita principe galiu trinti nes pasidariau geresni
def client_list():
    session = Session()
    clients= session.query(Client).all() #cia tiesiog susisiekiu su db ir iskvieciu visa client lista
    session.close()
    return render_template('client_list.html', clients=clients)

@app.route('/clients', methods=['GET', 'POST'])
def clients():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        tour_id = request.form['tour']  #jei rekvestas ateina su post metodu cia gaunu i inputus suvestus kliento duomenis

        session = Session()#susijungiu su duombaze
        tour = session.query(Tour).get(tour_id) #cia priskiriu konkretu tura klientui
        tour_name = tour.name #tour.name ateina is duombazes

        new_client = Client(name=name, surname=surname, email=email, tour_id=tour_id, tour_name=tour_name) #cia susikuria naujas Client objektas su touriD
        session.add(new_client) #issisaugo duombazeje
        session.commit()
        session.close() #iraso ir sesija uzsidaro

        return redirect(url_for('clients')) #cia pasidarau kad likciau puslapyje po ikrovimo

    session = Session() #cia nauja sesija grazina man sarasa su visias klientais
    clients = session.query(Client).all() #gauname is db klientu lista
    tours = session.query(Tour).all()  #gauname turu lista,kuris bus rodomas per selekta
    session.close()
    return render_template('clients.html', clients=clients, tours=tours)
#sitie clients ir tours yra kintamieji kurie keliauja i clients.html, todel butinai turi buti nes pabires mano html

@app.route('/mtb_rila_rodopai')
def mtb_rila_rodopai():
    return render_template('mtb_rila_rodopai.html')

@app.route('/mtb_east_rodopai')
def mtb_east_rodopai():
    return render_template('mtb_east_rodopai.html')


@app.route('/delete_tour/<int:tour_id>', methods=['POST'])
def delete_tour(tour_id):
    session = Session()
    tour = session.query(Tour).get(tour_id) #susisieku su db ir trinu pasirinkta pagal id tura su delete metodu
    session.delete(tour)
    session.commit()
    session.close()
    return redirect(url_for('add_tour')) #kadangi delete tour pas mane add puslapyje, tai ten ir pasilieku


#render_template-atvaizduoja HTML šabloną ir grąžina jį kaip atsakymą klientui.
#request-suteikia prieigą prie užklausos duomenų, kuriuos siunčia klientas, įskaitant formos duomenis, užklausos parametrus, cookies ir pan.
#redirect-nukreipia kitu ma6rutu, pvz po formos pateikimo
#url_for- tiesog kaip linkas kur eiti, su redirektu kartu gali b8ti
