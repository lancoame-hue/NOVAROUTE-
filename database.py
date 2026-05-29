class Destinazione:
    def __init__(self, nome, paese, budget, clima, paesaggio, mood, esperienze,sicurezza, stagione, rating, famiglia=False, disabilita=False):

        """Classe Modello: Rappresenta una singola meta turistica con i suoi attributi. Ogni parametro (nome, paese, ecc.) è di tipo 'str' o 'int' a seconda del valore."""

        # --- ATTRIBUTI (DATI) ---
        self.nome = nome                # Identificatore della città o località (tipo: str).
        self.paese = paese              # Nazione di appartenenza (tipo: str).
        self.budget = budget            # Fascia di prezzo: 1=Economico, 2=Medio, 3=Lusso (tipo: int).
        self.clima = clima              # Tipologia climatica, es. 'Caldo', 'Freddo' (tipo: str).
        self.paesaggio = paesaggio      # Ambiente naturale, es. 'Mare', 'Montagna' (tipo: str).
        self.mood = mood                # Atmosfera del viaggio, es. 'Relax', 'Avventura' (tipo: str).
        self.esperienze = esperienze    # Lista di attività disponibili (tipo: list).
        self.sicurezza = sicurezza      # Livello di incolumità per il viaggiatore (tipo: int).
        self.stagione = stagione        # Periodo ideale per la visita (tipo: str).
        self.rating = rating            # Punteggio globale di popolarità (tipo: float/int).
        self.famiglia = famiglia        # Idoneità per viaggi con bambini (tipo: bool, default: False).
        self.disabilita = disabilita    # Presenza di infrastrutture accessibili (tipo: bool, default: False).

        # --- LOGICA DI GEOLOCALIZZAZIONE ---
        europa = {
            "Italia","Francia","Spagna","Germania","Austria","Svizzera","Olanda",
            "Belgio","Portogallo","Grecia","Repubblica Ceca","Ungheria","Irlanda",
            "Svezia","Islanda","Norvegia","Danimarca","Finlandia","Polonia",
            "Romania","Croazia","Slovenia","Slovacchia","Regno Unito"
        }
        
        # Permette al filtro geografico dell'app di separare le mete "vicine" da quelle "lontane".
        if paese in europa:
            self.continente = "Europa"
        else:
            self.continente = "Mondo"

# Destinazione(nome, continente, budget, clima, paesaggio, mood, esperienze, sicurezza, stagione, famiglia, disabilita)

def crea_database():
    # ====================== 100 DESTINAZIONI BILANCIATE ======================
    destinazioni = [
        # ===================== EUROPA (40) =====================
        # ===================== ITALIA =====================
            Destinazione("Roma","Italia",140,"Mediterraneo",["Citta"],["Cultura","Romantico"],["Visite culturali / musei","Esperienze enogastronomiche","Festival e eventi"],6,"Primavera",9,True,True),
            Destinazione("Milano","Italia",160,"Fresco",["Citta"],["Lusso","Moderno"],["Esperienze enogastronomiche","Festival e eventi"],5,"Autunno",8,True,True),
            Destinazione("Venezia","Italia",220,"Mediterraneo",["Mare"],["Romantico"],["Tour in barca o crociera","Visite culturali / musei"],5,"Primavera",9,True,False),
            Destinazione("Napoli","Italia",90,"Mediterraneo",["Mare"],["Gastronomico"],["Esperienze enogastronomiche","Tour in barca o crociera"],4,"Estate",8,True,False),
            Destinazione("Firenze","Italia",150,"Mediterraneo",["Citta"],["Cultura"],["Visite culturali / musei"],6,"Primavera",9,True,True),
            Destinazione("Palermo","Italia",85,"Mediterraneo",["Citta"],["Cultura","Gastronomico"],["Esperienze enogastronomiche","Visite culturali / musei"],4,"Estate",7,True,False),
            Destinazione("Cinque Terre","Italia",180,"Mediterraneo",["Mare"],["Relax"],["Escursioni e trekking","Tour in barca o crociera"],5,"Primavera",9,True,False),
            Destinazione("Cortina","Italia",300,"Montano",["Montagne"],["Avventura"],["Escursioni e trekking","Sport acquatici o estremi"],9,"Inverno",9,True,False),
            Destinazione("Siena","Italia",120,"Mediterraneo",["Citta"],["Cultura"],["Visite culturali / musei","Festival e eventi"],7,"Autunno",8,True,True),
            Destinazione("Verona","Italia",130,"Mediterraneo",["Citta"],["Romantico"],["Visite culturali / musei","Festival e eventi"],6,"Primavera",9,True,True),

            # ===================== FRANCIA =====================
            Destinazione("Parigi","Francia",250,"Oceanico",["Citta"],["Romantico","Cultura"],["Visite culturali / musei","Esperienze enogastronomiche"],5,"Primavera",10,True,True),
            Destinazione("Nizza","Francia",180,"Mediterraneo",["Mare"],["Relax"],["Tour in barca o crociera","Relax in spa / wellness"],6,"Estate",9,True,True),
            Destinazione("Lione","Francia",130,"Fresco",["Citta"],["Gastronomico"],["Esperienze enogastronomiche"],6,"Autunno",8,True,True),
            Destinazione("Bordeaux","Francia",140,"Oceanico",["Citta"],["Relax"],["Esperienze enogastronomiche"],7,"Estate",8,True,True),
            Destinazione("Marsiglia","Francia",110,"Mediterraneo",["Mare"],["Cultura"],["Tour in barca o crociera","Visite culturali / musei"],4,"Estate",8,True,False),

            # ===================== SPAGNA =====================
            Destinazione("Barcellona","Spagna",130,"Mediterraneo",["Citta"],["Nightlife","Cultura"],["Visite culturali / musei","Festival e eventi"],5,"Estate",10,True,True),
            Destinazione("Madrid","Spagna",120,"Mediterraneo",["Citta"],["Cultura"],["Visite culturali / musei"],5,"Primavera",9,True,True),
            Destinazione("Siviglia","Spagna",100,"Mediterraneo",["Citta"],["Cultura"],["Festival e eventi","Visite culturali / musei"],5,"Primavera",9,True,True),
            Destinazione("Granada","Spagna",90,"Mediterraneo",["Citta"],["Cultura"],["Visite culturali / musei"],5,"Primavera",9,True,True),
            Destinazione("Ibiza","Spagna",350,"Mediterraneo",["Mare"],["Nightlife"],["Festival e eventi","Sport acquatici o estremi"],6,"Estate",10,False,False),

            # ===================== EUROPA VARIA =====================
            Destinazione("Berlino","Germania",110,"Fresco",["Citta"],["Nightlife","Cultura"],["Festival e eventi","Visite culturali / musei"],6,"Autunno",10,True,True),
            Destinazione("Monaco","Germania",140,"Fresco",["Citta","Montagne"],["Cultura"],["Festival e eventi","Escursioni e trekking"],7,"Estate",9,True,True),
            Destinazione("Amburgo","Germania",120,"Oceanico",["Mare"],["Cultura"],["Tour in barca o crociera","Festival e eventi"],6,"Estate",8,True,True),
            Destinazione("Londra","Regno Unito",200,"Oceanico",["Citta"],["Cultura"],["Visite culturali / musei","Festival e eventi"],5,"Tutto l'anno",10,True,True),
            Destinazione("Edimburgo","Regno Unito",150,"Oceanico",["Montagne"],["Cultura"],["Festival e eventi","Escursioni e trekking"],7,"Estate",9,True,True),
            Destinazione("Dublino","Irlanda",160,"Oceanico",["Citta"],["Nightlife"],["Festival e eventi"],6,"Estate",9,True,True),
            Destinazione("Amsterdam","Olanda",180,"Oceanico",["Citta"],["Relax","Cultura"],["Tour in barca o crociera","Visite culturali / musei"],6,"Primavera",10,True,True),
            Destinazione("Praga","Repubblica Ceca",85,"Fresco",["Citta"],["Romantico"],["Visite culturali / musei"],7,"Autunno",9,True,True),
            Destinazione("Budapest","Ungheria",80,"Fresco",["Citta"],["Relax"],["Relax in spa / wellness"],6,"Autunno",10,True,True),
            Destinazione("Vienna","Austria",140,"Fresco",["Citta"],["Cultura"],["Visite culturali / musei"],8,"Primavera",9,True,True),

            Destinazione("Atene", "Grecia", 140, "Mediterraneo", ["Città", "Mare"], ["Cultura"], ["Visite culturali / musei", "Festival e eventi"], 5, "Primavera", 10, True, True),
            Destinazione("Santorini", "Grecia", 200, "Mediterraneo", ["Mare", "Città"], ["Romantico", "Relax"], ["Relax in spa / wellness", "Tour in barca o crociera"], 5, "Estate", 10, False, False),
            Destinazione("Creta", "Grecia", 110, "Mediterraneo", ["Mare", "Montagne"], ["Avventura", "Relax"], ["Escursioni e trekking", "Tour in barca o crociera"], 5, "Estate", 9, True, False),
            Destinazione("Rodi", "Grecia", 100, "Mediterraneo", ["Mare", "Città"], ["Cultura", "Relax"], ["Visite culturali / musei"], 5, "Estate", 9, True, False),
            Destinazione("Salonicco", "Grecia", 80, "Mediterraneo", ["Città", "Mare"], ["Cultura", "Gastronomico"], ["Esperienze enogastronomiche", "Festival e eventi"], 5, "Autunno", 8, True, True),

            Destinazione("Lisbona", "Portogallo", 110, "Oceanico", ["Città", "Mare"], ["Cultura", "Relax"], ["Visite culturali / musei", "Esperienze enogastronomiche"], 6, "Primavera", 9, True, True),
            Destinazione("Porto", "Portogallo", 90, "Oceanico", ["Città"], ["Gastronomico", "Cultura"], ["Esperienze enogastronomiche"], 7, "Autunno", 9, True, True),
            Destinazione("Algarve", "Portogallo", 130, "Mediterraneo", ["Mare"], ["Relax"], ["Sport acquatici o estremi", "Tour in barca o crociera"], 6, "Estate", 9, True, False),

            Destinazione("Copenaghen", "Danimarca", 160, "Freddo", ["Città"], ["Cultura"], ["Visite culturali / musei"], 8, "Estate", 9, True, True),
            Destinazione("Stoccolma", "Svezia", 170, "Freddo", ["Città"], ["Cultura"], ["Visite culturali / musei"], 8, "Estate", 9, True, True),
            Destinazione("Oslo", "Norvegia", 180, "Freddo", ["Città", "Montagne"], ["Avventura", "Cultura"], ["Escursioni e trekking"], 9, "Estate", 9, True, True),
            Destinazione("Reykjavik", "Islanda", 250, "Freddo", ["Montagne", "Neve"], ["Avventura", "Relax"], ["Escursioni e trekking", "Relax in spa / wellness"], 10, "Estate", 9, True, False),

            Destinazione("Zurigo", "Svizzera", 280, "Freddo", ["Città", "Lago"], ["Lusso"], ["Relax in spa / wellness"], 9, "Inverno", 9, True, True),
            Destinazione("Ginevra", "Svizzera", 260, "Freddo", ["Città", "Lago"], ["Lusso", "Cultura"], ["Visite culturali / musei"], 8, "Estate", 8, True, True),
            Destinazione("Bruges", "Belgio", 150, "Oceanico", ["Città"], ["Romantico", "Cultura"], ["Visite culturali / musei"], 6, "Primavera", 9, True, True),

            Destinazione("Rotterdam", "Olanda", 160, "Oceanico", ["Città"], ["Cultura"], ["Visite culturali / musei"], 7, "Estate", 8, True, True),
            Destinazione("Bruxelles", "Belgio", 150, "Oceanico", ["Città"], ["Cultura", "Gastronomico"], ["Esperienze enogastronomiche"], 6, "Primavera", 8, True, True),

            Destinazione("Lucerna", "Svizzera", 240, "Freddo", ["Lago", "Montagne"], ["Relax", "Romantico"], ["Escursioni e trekking"], 9, "Estate", 9, True, True),
            Destinazione("Lubiana", "Slovenia", 100, "Fresco", ["Città"], ["Cultura", "Relax"], ["Visite culturali / musei"], 8, "Primavera", 9, True, True),
            Destinazione("Bratislava", "Slovacchia", 90, "Fresco", ["Città"], ["Cultura"], ["Visite culturali / musei"], 7, "Autunno", 8, True, True),
            Destinazione("Cracovia", "Polonia", 80, "Fresco", ["Città"], ["Cultura", "Romantico"], ["Visite culturali / musei"], 7, "Primavera", 9, True, True),
            Destinazione("Varsavia", "Polonia", 85, "Fresco", ["Città"], ["Cultura"], ["Visite culturali / musei"], 7, "Estate", 8, True, True),

            Destinazione("Bucarest", "Romania", 75, "Fresco", ["Città"], ["Cultura", "Nightlife"], ["Festival e eventi"], 6, "Autunno", 8, True, True),
            Destinazione("Transilvania", "Romania", 90, "Fresco", ["Montagne", "Foresta"], ["Avventura"], ["Escursioni e trekking"], 8, "Estate", 9, True, False),

            Destinazione("Dubrovnik", "Croazia", 150, "Mediterraneo", ["Città", "Mare"], ["Cultura", "Romantico"], ["Tour in barca o crociera"], 6, "Estate", 9, True, True),
            Destinazione("Spalato", "Croazia", 120, "Mediterraneo", ["Città", "Mare"], ["Relax", "Cultura"], ["Tour in barca o crociera"], 6, "Estate", 8, True, True),

            Destinazione("Helsinki", "Finlandia", 160, "Freddo", ["Città", "Mare"], ["Relax", "Cultura"], ["Relax in spa / wellness"], 9, "Estate", 9, True, True),
            Destinazione("Aarhus", "Danimarca", 140, "Freddo", ["Città"], ["Cultura"], ["Visite culturali / musei"], 9, "Estate", 8, True, True),
            Destinazione("Goteborg", "Svezia", 150, "Freddo", ["Città", "Mare"], ["Relax", "Cultura"], ["Esperienze enogastronomiche"], 9, "Estate", 8, True, True),
            Destinazione("Bergen", "Norvegia", 180, "Freddo", ["Montagne"], ["Avventura", "Relax"], ["Escursioni e trekking"], 10, "Estate", 9, True, True),
            Destinazione("Akureyri", "Islanda", 220, "Freddo", ["Montagne", "Neve"], ["Avventura"], ["Escursioni e trekking"], 10, "Estate", 8, True, False),
            
            # ===================== ASIA (25) =====================
            # GIAPPONE (4)
            Destinazione("Tokyo", "Giappone", 300, "Fresco", ["Citta"], ["Visite culturali / musei"], ["Escursioni e trekking", "Festival e eventi"], 8, "Primavera", 10, True, True),
            Destinazione("Kyoto", "Giappone", 250, "Fresco", ["Citta", "Montagne"], ["Visite culturali / musei", "Relax in spa / wellness"], ["Escursioni e trekking"], 9, "Primavera", 9, True, True),
            Destinazione("Osaka", "Giappone", 200, "Fresco", ["Citta"], ["Esperienze enogastronomiche", "Festival e eventi"], ["Festival e eventi"], 6, "Autunno", 9, True, True),
            Destinazione("Hokkaido", "Giappone", 220, "Freddo", ["Montagne", "Neve"], ["Escursioni e trekking", "Sport acquatici o estremi"], ["Sport acquatici o estremi", "Escursioni e trekking"], 10, "Inverno", 9, True, False),

            # CINA (3)
            Destinazione("Pechino", "Cina", 180, "Fresco", ["Citta"], ["Visite culturali / musei"], ["Visite culturali / musei"], 5, "Autunno", 9, True, True),
            Destinazione("Shanghai", "Cina", 220, "Fresco", ["Citta"], ["Visite culturali / musei"], ["Festival e eventi"], 5, "Autunno", 9, True, True),
            Destinazione("Zhangjiajie", "Cina", 120, "Fresco", ["Montagne", "Foresta"], ["Escursioni e trekking"], ["Escursioni e trekking"], 7, "Estate", 8, True, False),

            # COREA (2)
            Destinazione("Seoul", "Corea del Sud", 280, "Fresco", ["Citta"], ["Visite culturali / musei"], ["Festival e eventi"], 6, "Primavera", 10, True, True),
            Destinazione("Busan", "Corea del Sud", 180, "Fresco", ["Citta", "Mare"], ["Relax in spa / wellness"], ["Sport acquatici o estremi"], 5, "Estate", 9, True, True),

            # SUD-EST ASIATICO (8)
            Destinazione("Bangkok", "Thailandia", 70, "Tropicale", ["Citta"], ["Esperienze enogastronomiche"], ["Festival e eventi"], 4, "Inverno", 9, True, True),
            Destinazione("Chiang Mai", "Thailandia", 60, "Tropicale", ["Citta", "Montagne"], ["Escursioni e trekking"], ["Attività con animali (safari, ecc.)"], 5, "Inverno", 9, True, True),
            Destinazione("Phuket", "Thailandia", 100, "Tropicale", ["Mare"], ["Sport acquatici o estremi"], ["Sport acquatici o estremi"], 4, "Inverno", 9, True, False),
            Destinazione("Bali", "Indonesia", 90, "Tropicale", ["Mare", "Montagne"], ["Relax in spa / wellness"], ["Relax in spa / wellness"], 5, "Estate", 10, True, False),
            Destinazione("Singapore", "Singapore", 350, "Tropicale", ["Citta"], ["Visite culturali / musei"], ["Festival e eventi"], 10, "Tutto l'anno", 10, True, True),
            Destinazione("Hanoi", "Vietnam", 90, "Tropicale", ["Citta", "Lago"], ["Visite culturali / musei"], ["Tour in barca o crociera"], 5, "Inverno", 9, True, True),
            Destinazione("Ho Chi Minh", "Vietnam", 85, "Tropicale", ["Citta"], ["Visite culturali / musei"], ["Festival e eventi"], 4, "Inverno", 8, True, True),
            Destinazione("Angkor Wat", "Cambogia", 80, "Tropicale", ["Citta", "Foresta"], ["Visite culturali / musei"], ["Escursioni e trekking"], 4, "Inverno", 8, True, False),

            # INDIA (3)
            Destinazione("Delhi", "India", 70, "Tropicale", ["Citta"], ["Visite culturali / musei"], ["Esperienze enogastronomiche"], 4, "Inverno", 8, True, True),
            Destinazione("Jaipur", "India", 65, "Tropicale", ["Citta", "Deserto"], ["Visite culturali / musei"], ["Escursioni e trekking"], 5, "Inverno", 8, True, True),
            Destinazione("Kerala", "India", 80, "Tropicale", ["Mare", "Foresta"], ["Relax in spa / wellness"], ["Tour in barca o crociera"], 5, "Inverno", 9, True, False),

            # MEDIO ORIENTE (5)
            Destinazione("Dubai", "Emirati Arabi", 500, "Deserto", ["Citta", "Deserto"], ["Visite culturali / musei"], ["Sport acquatici o estremi"], 8, "Inverno", 10, True, True),
            Destinazione("Abu Dhabi", "Emirati Arabi", 450, "Deserto", ["Citta", "Deserto"], ["Visite culturali / musei"], ["Relax in spa / wellness"], 9, "Inverno", 10, True, True),
            Destinazione("Doha", "Qatar", 400, "Deserto", ["Citta", "Deserto"], ["Visite culturali / musei"], ["Festival e eventi"], 8, "Inverno", 9, True, True),
            Destinazione("Tel Aviv", "Israele", 180, "Mediterraneo", ["Citta", "Mare"], ["Relax in spa / wellness"], ["Sport acquatici o estremi"], 5, "Primavera", 9, True, True),
            Destinazione("Gerusalemme", "Israele", 150, "Mediterraneo", ["Citta"], ["Visite culturali / musei"], ["Visite culturali / musei"], 4, "Primavera", 8, True, False),

            # USA (8)
            Destinazione("New York", "USA", 400, "Fresco", ["Citta"], ["Visite culturali / musei"], ["Festival e eventi"], 5, "Autunno", 10, True, True),
            Destinazione("Los Angeles", "USA", 350, "Mediterraneo", ["Citta", "Mare"], ["Relax in spa / wellness"], ["Sport acquatici o estremi"], 5, "Estate", 10, True, True),
            Destinazione("San Francisco", "USA", 350, "Mediterraneo", ["Citta", "Mare"], ["Visite culturali / musei"], ["Tour in barca o crociera"], 5, "Estate", 9, True, True),
            Destinazione("Las Vegas", "USA", 300, "Deserto", ["Citta", "Deserto"], ["Festival e eventi"], ["Festival e eventi"], 5, "Tutto l'anno", 10, False, True),
            Destinazione("Chicago", "USA", 280, "Fresco", ["Citta", "Lago"], ["Visite culturali / musei"], ["Esperienze enogastronomiche"], 5, "Estate", 8, True, True),
            Destinazione("Miami", "USA", 320, "Tropicale", ["Mare", "Citta"], ["Relax in spa / wellness"], ["Sport acquatici o estremi"], 4, "Inverno", 9, True, True),
            Destinazione("Seattle", "USA", 280, "Oceanico", ["Citta", "Lago"], ["Visite culturali / musei"], ["Escursioni e trekking"], 6, "Estate", 8, True, True),
            Destinazione("Denver", "USA", 250, "Montano", ["Citta", "Montagne"], ["Escursioni e trekking"], ["Sport acquatici o estremi"], 7, "Inverno", 8, True, True),

            # ===================== CANADA (3) =====================
            Destinazione("Toronto", "Canada", 220, "Freddo", ["Città", "Lago"], ["Visite culturali / musei"], ["Visite culturali / musei", "Attività con animali (safari, ecc.)", "Festival e eventi"], 7, "Estate", 9, True, True),
            Destinazione("Vancouver", "Canada", 250, "Oceanico", ["Città", "Montagne"], ["Escursioni e trekking", "Natura"], ["Sport acquatici o estremi", "Escursioni e trekking", "Visite culturali / musei"], 8, "Estate", 9, True, True),
            Destinazione("Montreal", "Canada", 200, "Freddo", ["Città"], ["Visite culturali / musei", "Esperienze enogastronomiche"], ["Esperienze enogastronomiche", "Festival e eventi", "Visite culturali / musei"], 6, "Estate", 8, True, True),

            # ===================== AMERICA CENTRALE (2) =====================
            Destinazione("Costa Rica", "Costa Rica", 120, "Tropicale", ["Foresta", "Mare"], ["Escursioni e trekking", "Natura"], ["Sport acquatici o estremi", "Attività con animali (safari, ecc.)", "Escursioni e trekking"], 6, "Inverno", 9, True, False),
            Destinazione("Tulum", "Messico", 150, "Tropicale", ["Mare", "Deserto"], ["Relax in spa / wellness", "Visite culturali / musei"], ["Visite culturali / musei", "Sport acquatici o estremi", "Relax in spa / wellness"], 5, "Inverno", 8, True, False),

            # ===================== AMERICA LATINA (7) =====================
            Destinazione("Città del Messico", "Messico", 100, "Tropicale", ["Città"], ["Visite culturali / musei", "Esperienze enogastronomiche"], ["Visite culturali / musei", "Esperienze enogastronomiche", "Festival e eventi"], 4, "Primavera", 8, True, True),
            Destinazione("Cancun", "Messico", 180, "Tropicale", ["Mare"], ["Relax in spa / wellness", "Festival e eventi"], ["Sport acquatici o estremi", "Relax in spa / wellness", "Festival e eventi"], 4, "Inverno", 9, True, False),
            Destinazione("Rio de Janeiro", "Brasile", 250, "Tropicale", ["Mare", "Città"], ["Festival e eventi", "Escursioni e trekking"], ["Festival e eventi", "Sport acquatici o estremi", "Escursioni e trekking"], 4, "Estate", 10, True, False),
            Destinazione("San Paolo", "Brasile", 220, "Tropicale", ["Città"], ["Visite culturali / musei", "Esperienze enogastronomiche"], ["Visite culturali / musei", "Esperienze enogastronomiche", "Festival e eventi"], 4, "Estate", 8, True, True),
            Destinazione("Buenos Aires", "Argentina", 220, "Fresco", ["Città"], ["Visite culturali / musei", "Festival e eventi"], ["Festival e eventi", "Esperienze enogastronomiche", "Visite culturali / musei"], 5, "Primavera", 9, True, True),
            Destinazione("Santiago", "Cile", 180, "Mediterraneo", ["Città", "Montagne"], ["Escursioni e trekking", "Visite culturali / musei"], ["Esperienze enogastronomiche", "Escursioni e trekking", "Visite culturali / musei"], 6, "Estate", 8, True, True),
            Destinazione("Lima", "Perù", 120, "Mediterraneo", ["Città", "Mare"], ["Esperienze enogastronomiche", "Visite culturali / musei"], ["Esperienze enogastronomiche", "Visite culturali / musei", "Tour in barca o crociera"], 5, "Estate", 7, True, True),
            Destinazione("Cusco", "Perù", 100, "Montano", ["Montagne", "Città"], ["Escursioni e trekking", "Visite culturali / musei"], ["Escursioni e trekking", "Visite culturali / musei", "Attività con animali (safari, ecc.)"], 6, "Estate", 7, True, False),

            # ===================== AFRICA (10) =====================
            Destinazione("Marrakech", "Marocco", 80, "Tropicale", ["Città", "Deserto"], ["Visite culturali / musei", "Esperienze enogastronomiche"], ["Visite culturali / musei", "Esperienze enogastronomiche", "Festival e eventi"], 5, "Primavera", 9, True, False),
            Destinazione("Casablanca", "Marocco", 90, "Tropicale", ["Città", "Mare"], ["Visite culturali / musei", "Esperienze enogastronomiche"], ["Visite culturali / musei", "Festival e eventi", "Esperienze enogastronomiche"], 5, "Primavera", 8, True, True),
            Destinazione("Fes", "Marocco", 70, "Tropicale", ["Città"], ["Visite culturali / musei"], ["Visite culturali / musei", "Esperienze enogastronomiche"], 5, "Primavera", 8, True, False),
            Destinazione("Il Cairo", "Egitto", 100, "Deserto", ["Città", "Deserto"], ["Visite culturali / musei"], ["Visite culturali / musei", "Escursioni e trekking"], 4, "Inverno", 9, True, False),
            Destinazione("Luxor", "Egitto", 90, "Deserto", ["Città", "Deserto"], ["Visite culturali / musei"], ["Visite culturali / musei", "Escursioni e trekking"], 4, "Inverno", 8, True, False),
            Destinazione("Sharm el Sheikh", "Egitto", 120, "Deserto", ["Mare", "Deserto"], ["Relax in spa / wellness", "Sport acquatici o estremi"], ["Sport acquatici o estremi", "Relax in spa / wellness", "Attività con animali (safari, ecc.)"], 5, "Inverno", 8, True, False),
            Destinazione("Città del Capo", "Sudafrica", 200, "Mediterraneo", ["Mare", "Montagne"], ["Escursioni e trekking", "Natura"], ["Attività con animali (safari, ecc.)", "Escursioni e trekking", "Esperienze enogastronomiche"], 6, "Estate", 9, True, False),
            Destinazione("Johannesburg", "Sudafrica", 150, "Mediterraneo", ["Città"], ["Visite culturali / musei"], ["Visite culturali / musei", "Festival e eventi"], 5, "Estate", 7, True, True),
            Destinazione("Victoria Falls", "Zambia/Zimbabwe", 180, "Tropicale", ["Natura", "Acqua"], ["Escursioni e trekking", "Sport acquatici o estremi"], ["Sport acquatici o estremi", "Attività con animali (safari, ecc.)", "Escursioni e trekking"], 6, "Estate", 7, True, False),
            Destinazione("Zanzibar", "Tanzania", 130, "Tropicale", ["Mare"], ["Relax in spa / wellness", "Visite culturali / musei"], ["Sport acquatici o estremi", "Relax in spa / wellness", "Visite culturali / musei"], 5, "Estate", 7, True, False),
            Destinazione("Tangeri", "Marocco", 85, "Mediterraneo", ["Città", "Mare"], ["Visite culturali / musei"], ["Visite culturali / musei", "Esperienze enogastronomiche"], 5, "Primavera", 7, True, False),

            # ===================== OCEANIA (5) =====================
            Destinazione("Sydney", "Australia", 320, "Mediterraneo", ["Città", "Mare"], ["Escursioni e trekking", "Relax in spa / wellness"], ["Sport acquatici o estremi", "Escursioni e trekking", "Festival e eventi"], 8, "Inverno", 10, True, True),
            Destinazione("Melbourne", "Australia", 280, "Mediterraneo", ["Città"], ["Visite culturali / musei", "Esperienze enogastronomiche"], ["Visite culturali / musei", "Esperienze enogastronomiche", "Festival e eventi"], 7, "Inverno", 9, True, True),
            Destinazione("Brisbane", "Australia", 250, "Mediterraneo", ["Città", "Mare"], ["Relax in spa / wellness", "Escursioni e trekking"], ["Sport acquatici o estremi", "Escursioni e trekking", "Attività con animali (safari, ecc.)"], 7, "Inverno", 9, True, True),
            Destinazione("Auckland", "Nuova Zelanda", 260, "Oceanico", ["Città", "Mare"], ["Escursioni e trekking", "Natura"], ["Escursioni e trekking", "Sport acquatici o estremi", "Visite culturali / musei"], 8, "Estate", 9, True, True),
            Destinazione("Queenstown", "Nuova Zelanda", 300, "Freddo", ["Montagne", "Lago"], ["Escursioni e trekking", "Sport acquatici o estremi"], ["Sport acquatici o estremi", "Escursioni e trekking"], 9, "Inverno", 9, True, False),
        
            # ===================== ALTRI ASIA (Mancanti per arrivare a 25) =====================
            Destinazione("Kathmandu", "Nepal", 60, "Montano", ["Montagne", "Città"], ["Escursioni e trekking", "Visite culturali / musei"], ["Escursioni e trekking", "Attività con animali (safari, ecc.)", "Visite culturali / musei"], 7, "Primavera", 7, True, False),
            Destinazione("Mumbai", "India", 90, "Tropicale", ["Città", "Mare"], ["Nightlife e movida", "Visite culturali / musei"], ["Nightlife e movida", "Esperienze enogastronomiche", "Visite culturali / musei"], 3, "Inverno", 8, True, True),
            Destinazione("Goa", "India", 80, "Tropicale", ["Mare"], ["Relax in spa / wellness", "Nightlife e movida"], ["Relax in spa / wellness", "Sport acquatici o estremi", "Nightlife e movida"], 4, "Inverno", 8, True, False),
            Destinazione("Luang Prabang", "Laos", 55, "Tropicale", ["Città", "Montagne"], ["Visite culturali / musei", "Relax in spa / wellness"], ["Visite culturali / musei", "Relax in spa / wellness", "Escursioni e trekking"], 6, "Inverno", 8, True, False),
            Destinazione("Siem Reap", "Cambogia", 50, "Tropicale", ["Città"], ["Visite culturali / musei"], ["Visite culturali / musei", "Escursioni e trekking", "Attività con animali (safari, ecc.)"], 4, "Inverno", 7, True, False),
            ]
    return destinazioni