# Moduli per la creazione dell'interfaccia utente (UI)
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton,QLineEdit, QHBoxLayout, QMessageBox, QGridLayout,QSlider, QSpinBox, QCheckBox, QFrame, QGraphicsDropShadowEffect,QSizePolicy
from PyQt5.QtCore import Qt, QRegExp
# Qt: Costanti di sistema (es. Qt.AlignCenter per centrare i testi).
# QRegExp: Espressioni regolari per definire filtri di ricerca o formati testo.

from PyQt5.QtGui import QIntValidator,QRegExpValidator,QColor
# QIntValidator: Blocca l'inserimento di lettere dove sono richiesti solo numeri (es. giorni).
# QRegExpValidator: Assicura che il testo inserito rispetti un formato specifico.
# QColor: Classe per definire i colori (RGB/RGBA) degli elementi grafici

# ====================== PAGINA 1: SCHERMATA INIZIALE ======================
class PaginaIniziale(QWidget): # Classe PaginaIniziale: Schermata di benvenuto
    def __init__(self, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;") ## background: transparent: Necessario per mostrare l'immagine di sfondo della FinestraPrincipale.

        # Layout principale con margini
        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 13, 60) 

        # --- 1.HEADER LOGO ---
        header_layout = QHBoxLayout()
        frame_titolo = QFrame() # frame_titolo (QFrame): Contenitore per lo stile visivo del titolo.
        frame_titolo.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 128, 120); 
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 30);
            }
        """)
        layout_titolo = QVBoxLayout(frame_titolo)
        layout_titolo.setContentsMargins(40, 15, 40, 15) # Spazio interno tra bordo e testo.
        
        lbl_titolo = QLabel("NOVAROUTE")
        lbl_titolo.setStyleSheet("""
            color: white; 
            font-size: 75px; 
            font-weight: 900; 
            letter-spacing: 12px; 
            background: transparent;
            border: none;
        """)
        lbl_titolo.setAlignment(Qt.AlignCenter)
        
        # glow_blu (QGraphicsDropShadowEffect): effetto estetico di retroilluminazione blu.
        glow_blu = QGraphicsDropShadowEffect()
        glow_blu.setBlurRadius(40) # Intensità della sfocatura.
        glow_blu.setColor(QColor(0, 150, 255, 255)) # Colore celeste luminoso.
        glow_blu.setOffset(0, 0) # L'effetto è centrato dietro al testo.
        lbl_titolo.setGraphicsEffect(glow_blu)
        
        layout_titolo.addWidget(lbl_titolo)
        header_layout.addWidget(frame_titolo)
        layout_principale.addLayout(header_layout)
        layout_principale.setAlignment(header_layout, Qt.AlignTop | Qt.AlignCenter)  # Allineamento in alto al centro per il titolo principale.

        # Spazio flessibile per spingere la frase verso il basso
        layout_principale.addStretch(16)

        # --- 2. FRASE ---
        frame_frase = QFrame() # frame_titolo (QFrame): Contenitore per lo stile visivo del titolo.
        frame_frase.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 128, 120); 
                border-radius: 15px;
                border: 1px solid rgba(255, 255, 255, 30);
            }
        """)
        layout_frase = QVBoxLayout(frame_frase)
        lbl_sotto = QLabel("Esplora il mondo, trova il tuo destino.")
        lbl_sotto.setStyleSheet("""
            color: white; font-size: 32px; font-weight: 600; 
            font-style: italic; border: none; background: transparent;
        """)
        lbl_sotto.setAlignment(Qt.AlignCenter)
        layout_frase.addWidget(lbl_sotto)
        layout_principale.addWidget(frame_frase, alignment=Qt.AlignCenter) # Allineamento in alto al centro per il titolo principale.


       # --- 3.PULSANTE DI AVVIO ---
        bott = QPushButton("INIZIA IL VIAGGIO →") # bott (QPushButton): Tasto interattivo per iniziare
        bott.setFixedSize(420, 85) # Dimensione fissa per mantenere l'estetica.
        # PointingHandCursor: Cambia il puntatore al passaggio del mouse.
        bott.setCursor(Qt.PointingHandCursor)
        bott.setStyleSheet("""
            QPushButton { 
                background-color: rgba(255, 255, 255, 0.25); 
                color:  #000080; 
                border: 2px solid white; 
                border-radius: 20px; 
                font-size: 22px;
                font-weight: bold;
                letter-spacing: 2px;
            } 
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """)
        bott.clicked.connect(callback_avanti)  # .clicked.connect: Collega il click alla funzione di navigazione della Main Window.
        layout_principale.addWidget(bott, alignment=Qt.AlignCenter)  # Allineamento in alto al centro per il titolo principale.

        self.setLayout(layout_principale)

# ====================== PAGINA 2: NOME ======================
class SecondaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(60, 50, 60, 50)
        layout_corpo.setSpacing(30)

        # Domanda Principale
        lbl_titolo = QLabel("BENVENUTO!\n\nCome ti posso chiamare?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 34px; font-weight: bold; background: none;")
        
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        # Input Nome 
        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Inserisci il tuo nome...")
        self.input_nome.setFixedSize(400, 60)
        self.input_nome.setAlignment(Qt.AlignCenter)
        self.input_nome.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #000080;
                border-radius: 15px;
                font-size: 22px;
                font-weight: bold;
                padding: 5px;
            }
        """)
        self.input_nome.returnPressed.connect(callback_avanti)
        layout_corpo.addWidget(self.input_nome, alignment=Qt.AlignCenter)

        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE ---
        layout_nav = QHBoxLayout()
        # Allinea verticalmente al centro per evitare altezze diverse
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; 
                color: white; 
                border: 2px solid white; 
                border-radius: 15px; 
                font-weight: bold; 
                font-size: 18px; 
            }
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        # Lo stretch agisce come una molla per allontanarli restando sulla stessa linea
        layout_nav.addStretch() 
        layout_nav.addWidget(btn_next)
        
        # Aggiungiamo il layout alla pagina
        layout_principale.addLayout(layout_nav)

# ====================== PAGINA 3: BENVENUTO ======================
class TerzaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(60, 60, 60, 60)
        layout_corpo.setSpacing(20)

        # Icona decorativa superiore
        lbl_icona = QLabel("🌍🗺️")
        lbl_icona.setStyleSheet("font-size: 60px; background: none; border: none;")
        lbl_icona.setAlignment(Qt.AlignCenter)
        layout_corpo.addWidget(lbl_icona)

        # Messaggio di Benvenuto (lbl3)
        self.lbl3 = QLabel("")
        self.lbl3.setAlignment(Qt.AlignCenter)
        self.lbl3.setStyleSheet("""
            color: white; 
            font-size: 38px; 
            font-weight: bold; 
            background: none; 
            border: none;
        """)
        
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        self.lbl3.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(self.lbl3)

        #--- INFO SOTTOTITOLO ---
        info = QLabel("Rispondi alle prossime domande e il nostro algoritmo\ntroverà la destinazione perfetta per te!")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("""
            color: rgb(0, 0, 128);
            font-size: 20px; 
            font-style: italic; 
            font-weight: 800;
            background-color: rgba(255, 255, 255, 0.5)
        """)
        
        layout_corpo.addWidget(info)

        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE ---
        layout_nav = QHBoxLayout()
        layout_nav.setContentsMargins(30, 0, 30, 0)
        # Forziamo l'allineamento centrale per mantenere entrambi i tasti sulla stessa linea
        layout_nav.setAlignment(Qt.AlignCenter) 
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; color: white; border: 2px solid white; 
                border-radius: 15px; font-weight: bold; font-size: 18px; 
            }
            QPushButton:hover { background-color: white; color: #000080; }
        """
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() # Spinge i tasti ai lati ma restano allineati
        layout_nav.addWidget(btn_next)
        layout_principale.addLayout(layout_nav)


    def aggiorna_nome(self, nome):
        # Messaggio reso più caloroso e centrato
        self.lbl3.setText(f"Ciao {nome}!")

# ====================== PAGINE 4: BUDGET ======================
class QuartaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")

        layout_principale = QVBoxLayout(self)
        # Coordinate richieste: 13, 13
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(60, 50, 60, 50)
        layout_corpo.setSpacing(35)

        # Domanda Principale
        lbl_titolo = QLabel("Qual è il tuo budget massimo a testa?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 34px; font-weight: bold; background: none;")
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        # Valore Budget Dinamico
        self.lbl_valore = QLabel("Budget: 100 €")
        self.lbl_valore.setAlignment(Qt.AlignCenter)
        self.lbl_valore.setStyleSheet("color: #00FFCC; font-size: 32px; font-weight: bold;")
        
        self.glow_valore = QGraphicsDropShadowEffect()
        self.glow_valore.setBlurRadius(25)
        self.glow_valore.setColor(QColor(0, 255, 204, 180))
        self.glow_valore.setOffset(0, 0)
        self.lbl_valore.setGraphicsEffect(self.glow_valore)
        layout_corpo.addWidget(self.lbl_valore)

        # Slider Budget
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(100)
        self.slider.setMaximum(50000)
        self.slider.setSingleStep(100)
        self.slider.setValue(100)
        self.slider.setFixedWidth(500)
        self.slider.setCursor(Qt.PointingHandCursor)
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #bbb;
                height: 12px;
                background: white;
                border-radius: 6px;
            }
            QSlider::handle:horizontal {
                background: white;
                border: 3px solid #000080;
                width: 26px;
                height: 26px;
                margin: -8px 0;
                border-radius: 13px;
            }
            QSlider::sub-page:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00FFCC, stop:0.5 #FFFF00, stop:1 #FF3366);
                border-radius: 6px;
            }
        """)
        self.slider.valueChanged.connect(self.aggiorna_etichetta)
        layout_corpo.addWidget(self.slider, alignment=Qt.AlignCenter)

        # --- SLIDER ---
        lbl_info = QLabel("Sposta la barra per definire il budget massimo")
        lbl_info.setAlignment(Qt.AlignCenter)
        lbl_info.setStyleSheet("""
            color: rgb(0, 0, 128); 
            font-size: 17px;
            font-style: italic; 
            font-weight: 800;
            background-color: rgba(255, 255, 255, 0.5);
        """)
        
        layout_corpo.addWidget(lbl_info, alignment=Qt.AlignCenter)

        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE  ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; 
                color: white; 
                border: 2px solid white; 
                border-radius: 15px; 
                font-weight: bold; 
                font-size: 18px; 
            }
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        # La molla (stretch) ora lavora solo in orizzontale
        layout_nav.addStretch() 
        layout_nav.addWidget(btn_next)
        
        layout_principale.addLayout(layout_nav)

    def aggiorna_etichetta(self, valore):
        formattato = f"{valore:,}".replace(",", ".")
        self.lbl_valore.setText(f"Budget: {formattato} €")
        
        if valore < 5000:
            colore = "#00FFCC"
        elif valore < 20000:
            colore = "#FFFF00"
        else:
            colore = "#FF3366"
            
        self.lbl_valore.setStyleSheet(f"color: {colore}; font-size: 32px; font-weight: bold;")
        self.glow_valore.setColor(QColor(colore))

# ====================== PAGINE 5: STAGIONE ======================
class QuintaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_stagione = ""

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(50, 50, 50, 50)
        layout_corpo.setSpacing(40)

        lbl_titolo = QLabel("In che stagione vuoi viaggiare?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 36px; font-weight: bold; background: none;")
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        # --- GRIGLIA STAGIONI ---
        grid = QGridLayout()
        grid.setSpacing(25)
        
        # Mappa stagioni
        self.stagioni_map = {
            "Primavera 🌸": (0, 0),
            "Estate ⛱️":    (0, 1),
            "Autunno 🍂":   (1, 0),
            "Inverno 🏂":   (1, 1),
            "Tutto l'anno 🌍": (2, 0) 
        }
        
        # Mappa valori reali
        self.valori_map = {
            "Primavera 🌸": "Primavera",
            "Estate ⛱️": "Estate",
            "Autunno 🍂": "Autunno",
            "Inverno 🏂": "Inverno",
            "Tutto l'anno 🌍": "Tutto l'anno"
        }
        
        self.bottoni = []
        self.style_normale = """
            QPushButton { background-color: white; color: #000080; font-weight: bold; border-radius: 20px; font-size: 18px; } 
            QPushButton:hover { background-color: #D6EAF8; }
        """
        self.style_selezionato = """
            QPushButton { background-color: #2E86C1; color: white; font-weight: bold; border-radius: 20px; border: 3px solid white; font-size: 18px; }
        """

        for testo, pos in self.stagioni_map.items():
            btn = QPushButton(testo)
            btn.setFixedSize(220, 80)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet(self.style_normale)
            btn.clicked.connect(self.seleziona)
            
            if testo == "Tutto l'anno 🌍":
                grid.addWidget(btn, 2, 0, 1, 2, alignment=Qt.AlignCenter)
            else:
                grid.addWidget(btn, pos[0], pos[1], alignment=Qt.AlignCenter)
            
            self.bottoni.append(btn)

        layout_corpo.addLayout(grid)
        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE CORRETTA ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        layout_nav.setSpacing(0)

        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; 
                color: white; 
                border: 2px solid white; 
                border-radius: 15px; 
                font-weight: bold; 
                font-size: 18px; 
            }
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """
        
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65) 
            b.setStyleSheet(style_nav)
        
        # Aggiunta al layout con stretch nel mezzo
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() # Spinge i tasti ai due lati opposti
        layout_nav.addWidget(btn_next)
        
        # Aggiunta al layout principale
        layout_principale.addLayout(layout_nav)

    def seleziona(self):
        bottone = self.sender()
        self.scelta_stagione = self.valori_map[bottone.text()]
        for btn in self.bottoni:
            if btn == bottone:
                btn.setStyleSheet(self.style_selezionato)
            else:
                btn.setStyleSheet(self.style_normale)

# ====================== PAGINE 6: DURATA VIAGGIO ======================
class SestaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13,13,20,50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(60, 50, 60, 50)
        layout_corpo.setSpacing(30)

        # Domanda Principale
        lbl_titolo = QLabel("Per quanti giorni vorresti stare via?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 34px; font-weight: bold; background: none;")
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        # Input Giorni
        self.input_giorni = QLineEdit()
        self.input_giorni.setPlaceholderText("Es: 7")
        self.input_giorni.setFixedSize(200, 60) # Leggermente più grande per visibilità
        self.input_giorni.setValidator(QIntValidator(1, 365))
        self.input_giorni.setMaxLength(3)
        self.input_giorni.setAlignment(Qt.AlignCenter)
        self.input_giorni.setStyleSheet("""
            QLineEdit {
                background-color: white;
                color: #000080;
                border-radius: 15px;
                font-size: 24px;
                font-weight: bold;
            }
        """)
        layout_corpo.addWidget(self.input_giorni, alignment=Qt.AlignCenter)

        lbl_info = QLabel("Inserisci un numero di giorni (1-365)")
        lbl_info.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        layout_corpo.addWidget(lbl_info, alignment=Qt.AlignCenter)

        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE CORRETTA ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; color: white; border: 2px solid white; 
                border-radius: 15px; font-weight: bold; font-size: 18px; 
            }
            QPushButton:hover { background-color: white; color: #000080; }
        """
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        # Aggiungi i widget e lo stretch nel mezzo
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() 
        layout_nav.addWidget(btn_next)
        
        layout_principale.addLayout(layout_nav)

# ====================== PAGINE 7: PERSONE + BAMBINI + DISABILITà ======================
class SettimaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.callback_avanti_originale = callback_avanti 

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("background-color: rgba(0, 0, 0, 30); border-radius: 30px; border: 1px solid rgba(255, 255, 255, 20);")
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(60, 40, 60, 40)
        layout_corpo.setSpacing(25)

        # --- DOMANDA PRINCIPALE  ---
        lbl_titolo = QLabel("Quante persone partecipano?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 34px; font-weight: bold; background: none;")
        
        # Applicazione dell'effetto ombra
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        
        layout_corpo.addWidget(lbl_titolo)

        stile_label = "color: white; font-size: 18px; font-weight: bold;"
        stile_input = "background-color: white; color: #000080; border-radius: 10px; padding: 5px; font-size: 18px; font-weight: bold;"

        # Totale persone
        tot_layout = QHBoxLayout()
        lbl_tot_text = QLabel("Totale persone:")
        lbl_tot_text.setStyleSheet(stile_label)
        tot_layout.addWidget(lbl_tot_text)
        self.spin_total = QSpinBox()
        self.spin_total.setRange(1, 30); self.spin_total.setValue(2); self.spin_total.setFixedSize(100, 40); self.spin_total.setStyleSheet(stile_input)
        tot_layout.addStretch(); tot_layout.addWidget(self.spin_total)
        layout_corpo.addLayout(tot_layout)

        # Bambini
        bam_layout = QHBoxLayout()
        lbl_bam_text = QLabel("Bambini (0-14 anni):")
        lbl_bam_text.setStyleSheet(stile_label)
        bam_layout.addWidget(lbl_bam_text)
        self.spin_bambini = QSpinBox()
        self.spin_bambini.setRange(0, 15); self.spin_bambini.setValue(0); self.spin_bambini.setFixedSize(100, 40); self.spin_bambini.setStyleSheet(stile_input)
        bam_layout.addStretch(); bam_layout.addWidget(self.spin_bambini)
        layout_corpo.addLayout(bam_layout)

        # --- ETÀ BAMBINI ---
        self.lbl_eta = QLabel("Età dei bambini (es. 5, 8, 12):")
        self.lbl_eta.setStyleSheet(stile_label)
        layout_corpo.addWidget(self.lbl_eta)
        
        self.input_eta = QLineEdit()
        self.input_eta.setPlaceholderText("Inserisci età separate da virgola")
        self.input_eta.setFixedSize(400, 45)
        self.input_eta.setStyleSheet(stile_input)
        
        reg_ex = QRegExp("[0-9,]*")
        self.input_eta.setValidator(QRegExpValidator(reg_ex, self.input_eta))
        layout_corpo.addWidget(self.input_eta)

        # Disabilità
        self.check_disabilita = QCheckBox("Ci sono persone con disabilità? 👨‍🦽")
        self.check_disabilita.setStyleSheet("""
            QCheckBox { color: white; font-size: 26px; font-weight: bold; spacing: 20px; background: transparent; padding-top: 10px; } 
            QCheckBox::indicator { width: 25px; height: 25px; border-radius: 8px; border: 2px solid white; background: rgba(255, 255, 255, 20); } 
            QCheckBox::indicator:checked { background-color: #3498DB; border: 2px solid #0096FF; }
        """)
        layout_corpo.addWidget(self.check_disabilita, alignment=Qt.AlignCenter)

        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(self.valida_e_procedi) 
        
        style_nav = """
            QPushButton { 
                background-color: transparent; color: white; border: 2px solid white; 
                border-radius: 15px; font-weight: bold; font-size: 18px; 
            }
            QPushButton:hover { background-color: white; color: #000080; }
        """
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() 
        layout_nav.addWidget(btn_next)
        layout_principale.addLayout(layout_nav)

    def valida_e_procedi(self):
        num_bambini = self.spin_bambini.value()
        num_totale = self.spin_total.value()
        testo = self.input_eta.text().strip()

        if num_bambini >= num_totale:
            self.mostra_errore("Il numero di bambini deve essere minore del\ntotale delle persone (serve almeno un adulto)!")
            return
        
        if num_bambini == 0 and testo:
            self.mostra_errore("Hai inserito delle età, ma il numero\ndi bambini è impostato a zero!")
            return
        
        if num_bambini > 0:
            if not testo:
                self.mostra_errore("Inserimento obbligatorio:\ninserisci l'età dei bambini!")
                return
            eta_pulite = [e for e in testo.split(',') if e.strip()]
            if len(eta_pulite) != num_bambini:
                self.mostra_errore(f"Hai indicato {num_bambini} bambini,\nma inserito {len(eta_pulite)} età!")
                return
            for e in eta_pulite:
                try:
                    valore = int(e)
                    if valore < 0 or valore > 14:
                        self.mostra_errore(f"L'età '{valore}' non è valida.\nInserisci numeri da 0 a 14.")
                        return
                except ValueError:
                    self.mostra_errore(f"L'input '{e} non è un numero valido!")
                    return
        self.callback_avanti_originale()

    def mostra_errore(self, messaggio):
        msg = QMessageBox(self)
        msg.setWindowTitle("Attenzione")
        msg.setText(messaggio)
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("QMessageBox { background-color: #f0f0f0; } QLabel { color: black; font-family: 'Arial'; font-size: 14px; qproperty-alignment: 'AlignCenter'; min-width: 300px; } QPushButton { background-color: #e1e1e1; color: black; border: 1px solid #adadad; border-radius: 3px; padding: 5px 20px; }")
        msg.exec_()

# ====================== PAGINA 8: CLIMA ======================
class OttavaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_clima = ""
        self.bottoni_clima = []

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13,13,20,50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(50, 50, 50, 50)
        layout_corpo.setSpacing(40)

        # Domanda Principale
        lbl_titolo = QLabel("Che tipo di clima preferisci?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 36px; font-weight: bold; background: none; border: none;")
        
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        # Griglia Climi
        grid = QGridLayout()
        grid.setSpacing(25)
        climi = ["Tropicale 🏝️", "Mediterraneo 🌊", "Fresco 🍂", "Freddo 🧊", "Montano ⛰️", "Oceanico 🌦️"]

        self.style_normale = """
            QPushButton { 
                background-color: white; color: #000080; 
                font-weight: bold; border-radius: 20px; font-size: 18px;
            } 
            QPushButton:hover { background-color: #D6EAF8; }
        """
        self.style_selezionato = """
            QPushButton {
                background-color: #2E86C1; color: white; 
                font-weight: bold; border-radius: 20px; border: 3px solid white; font-size: 18px;
            }
        """

        for i, testo in enumerate(climi):
            btn = QPushButton(testo)
            btn.setFixedSize(220, 80)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet(self.style_normale)
            btn.clicked.connect(self.seleziona)
            grid.addWidget(btn, i // 2, i % 2, alignment=Qt.AlignCenter)
            self.bottoni_clima.append(btn)

        layout_corpo.addLayout(grid)
        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)

        layout_principale.addStretch(2)

        # --- NAVIGAZIONE ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; 
                color: white; 
                border: 2px solid white; 
                border-radius: 15px; 
                font-weight: bold; 
                font-size: 18px; 
            }
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """
        
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() # Spinge i tasti ai lati opposti sulla stessa riga
        layout_nav.addWidget(btn_next)
        
        layout_principale.addLayout(layout_nav)

    def seleziona(self):
        bottone_cliccato = self.sender()
        self.scelta_clima = bottone_cliccato.text()
        for btn in self.bottoni_clima:
            if btn == bottone_cliccato:
                btn.setStyleSheet(self.style_selezionato)
            else:
                btn.setStyleSheet(self.style_normale)

# ====================== PAGINE 9: STATO/REGIONE ======================
class NonaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_regione = ""
        self.paese_input = ""
        self._callback_avanti = callback_avanti

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
                
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(60, 50, 60, 50)
        layout_corpo.setSpacing(25)

        # Domanda Principale
        lbl_titolo = QLabel("Dove vuoi viaggiare?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 36px; font-weight: bold; background: none; border: none;")
        
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        layout_corpo.addSpacing(10)

        # Opzioni di Viaggio
        self.bottoni = []
        opzioni = [
            ("🇪🇺 Europa", "europa"),
            ("🌍 Altri continenti", "mondo"),
            ("💡 Non ho idee", "random"),
        ]

        self.style_normale = """
            QPushButton { 
                background-color: white; color: #000080; 
                font-weight: bold; border-radius: 20px; font-size: 18px;
            } 
            QPushButton:hover { background-color: #D6EAF8; }
        """
        self.style_selezionato = """
            QPushButton {
                background-color: #2E86C1; color: white; 
                font-weight: bold; border-radius: 20px; border: 3px solid white; font-size: 18px;
            }
        """

        for testo, valore in opzioni:
            btn = QPushButton(testo)
            btn.setFixedSize(320, 75)
            btn.value = valore
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet(self.style_normale)
            btn.clicked.connect(self.seleziona)
            layout_corpo.addWidget(btn, alignment=Qt.AlignCenter)
            self.bottoni.append(btn)

        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; 
                color: white; 
                border: 2px solid white; 
                border-radius: 15px; 
                font-weight: bold; 
                font-size: 18px; 
            }
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """
        
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() # Molla orizzontale perfetta
        layout_nav.addWidget(btn_next)
        
        layout_principale.addLayout(layout_nav)

    def seleziona(self):
        btn = self.sender()
        self.scelta_regione = btn.value
        for b in self.bottoni:
            if b == btn:
                b.setStyleSheet(self.style_selezionato)
            else:
                b.setStyleSheet(self.style_normale)

# ====================== PAGINA 10: PAESAGGIO ======================
class DecimaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_paesaggio = []
        self.bottoni_paesaggio = {}

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(50, 50, 50, 50)
        layout_corpo.setSpacing(40)

        # Domanda Principale
        lbl_titolo = QLabel("Che tipo di paesaggio preferisci?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 36px; font-weight: bold; background: none; border: none;")
        
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        # Griglia Paesaggi
        grid = QGridLayout()
        grid.setSpacing(25)
        paesaggi = ["Mare 🏖️", "Montagne ⛰️", "Città 🏙️", "Foresta 🌲", 
                    "Lago 🏞️", "Deserto 🏜️", "Campagna 🌾", "Neve 🌨️"]

        self.style_normale = """
            QPushButton { 
                background-color: white; color: #000080; 
                font-weight: bold; border-radius: 20px; font-size: 18px;
            } 
            QPushButton:hover { background-color: #D6EAF8; }
        """
        self.style_selezionato = """
            QPushButton {
                background-color: #2E86C1; color: white; 
                font-weight: bold; border-radius: 20px; border: 3px solid white; font-size: 18px;
            }
        """

        for i, testo in enumerate(paesaggi):
            btn = QPushButton(testo)
            btn.setFixedSize(220, 80)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet(self.style_normale)
            btn.clicked.connect(self.seleziona)
            grid.addWidget(btn, i // 2, i % 2, alignment=Qt.AlignCenter)
            self.bottoni_paesaggio[testo] = btn

        layout_corpo.addLayout(grid)
        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)

        layout_principale.addStretch(2)

        # --- NAVIGAZIONE ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; 
                color: white; 
                border: 2px solid white; 
                border-radius: 15px; 
                font-weight: bold; 
                font-size: 18px; 
            }
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """
        
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() # Spinge i tasti ai lati opposti mantenendo l'allineamento
        layout_nav.addWidget(btn_next)
        
        # Aggiunta al layout principale
        layout_principale.addLayout(layout_nav)

    def seleziona(self):
        bottone = self.sender()
        testo = bottone.text()
        
        if testo in self.scelta_paesaggio:
            self.scelta_paesaggio.remove(testo)
            bottone.setStyleSheet(self.style_normale)
        else:
            if len(self.scelta_paesaggio) < 2:
                self.scelta_paesaggio.append(testo)
                bottone.setStyleSheet(self.style_selezionato)
            else:
                msg = QMessageBox(self)
                msg.setWindowTitle("Limite raggiunto")
                msg.setText("Puoi selezionare massimo 2 paesaggi!")
                msg.setIcon(QMessageBox.Warning)
                msg.setStyleSheet("""
                    QMessageBox { background-color: #f0f0f0; }
                    QLabel { color: black; font-family: 'Arial'; font-size: 14px; qproperty-alignment: 'AlignCenter'; min-width: 250px; }
                    QPushButton { background-color: #e1e1e1; color: black; border: 1px solid #adadad; border-radius: 3px; width: 80px; height: 25px; }
                """)
                msg.exec_()

# ====================== PAGINA 11: MOOD ======================
class UndicesimaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_mood = []
        self.bottoni_mood = {}

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        
        # Ombra per il Logo
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(15)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(2, 2)
        lbl_logo.setGraphicsEffect(ombra_logo)
        
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(50, 50, 50, 50)
        layout_corpo.setSpacing(40)

        # --- DOMANDA PRINCIPALE ---
        lbl_titolo = QLabel("Che mood di viaggio cerchi?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 36px; font-weight: bold; border: none; background: none;")
        
        # Ombra per la Domanda
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        
        layout_corpo.addWidget(lbl_titolo)

        # --- GRIGLIA MOOD ---
        grid = QGridLayout()
        grid.setSpacing(25)
        mood_list = ["Relax 🧘", "Avventura 🏔️", "Sport Estremi 🪂", 
                     "Lusso 💎", "Cultura 🏛️", "Famiglia 👨‍👧‍👦", 
                     "Romantico 💖", "Gastronomico 🍷", "Nightlife 🕺"]

        self.style_normale = """
            QPushButton { 
                background-color: white; color: #000080; 
                font-weight: bold; border-radius: 20px; font-size: 18px;
            } 
            QPushButton:hover { background-color: #D6EAF8; }
        """
        self.style_selezionato = """
            background-color: #2E86C1; color: white; 
            font-weight: bold; border-radius: 20px; border: 3px solid white; font-size: 18px;
        """

        for i, testo in enumerate(mood_list):
            btn = QPushButton(testo)
            btn.setFixedSize(220, 80)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet(self.style_normale)
            btn.clicked.connect(self.seleziona)
            grid.addWidget(btn, i // 3, i % 3, alignment=Qt.AlignCenter)
            self.bottoni_mood[testo] = btn

        layout_corpo.addLayout(grid)
        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)

        layout_principale.addStretch(2)

        # --- NAVIGAZIONE  ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; 
                color: white; 
                border: 2px solid white; 
                border-radius: 15px; 
                font-weight: bold; 
                font-size: 18px; 
            }
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """
        
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() 
        layout_nav.addWidget(btn_next)
        
        layout_principale.addLayout(layout_nav)

    def seleziona(self):
        bottone = self.sender()
        testo = bottone.text()
        
        if testo in self.scelta_mood:
            self.scelta_mood.remove(testo)
            bottone.setStyleSheet(self.style_normale)
        else:
            if len(self.scelta_mood) < 2:
                self.scelta_mood.append(testo)
                bottone.setStyleSheet(self.style_selezionato)
            else:
                # Messaggio in stile classico Arial e Nero
                msg = QMessageBox(self)
                msg.setWindowTitle("Limite raggiunto")
                msg.setText("Puoi selezionare massimo 2 mood!")
                msg.setIcon(QMessageBox.Warning) # Triangolo giallo classico
                
                msg.setStyleSheet("""
                    QMessageBox { 
                        background-color: #f0f0f0; 
                    }
                    QLabel { color: black; 
                        font-family: 'Arial'; 
                        font-size: 14px; 
                    }
                    QPushButton { 
                        background-color: #e1e1e1; color: black; border: 1px solid #adadad; border-radius: 3px;width: 80px;height: 25px; 
                    }
                    QPushButton:hover {background-color: #e5f1fb;border: 1px solid #0078d7;
                    }
                """)
                msg.exec_()

# ====================== PAGINA 12: ESPERIENZE ======================
class DodicesimaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")
        self.scelta_esperienze = []

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13,13,20,50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(50, 40, 50, 40)
        layout_corpo.setSpacing(30)

        lbl_titolo = QLabel("Quali esperienze vuoi vivere?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 34px; font-weight: bold; background: none;")
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        grid_esperienze = QGridLayout()
        grid_esperienze.setSpacing(20)
        self.checks = []
        esperienze = [
            "Escursioni e trekking 🥾", "Visite culturali 🏛️", 
            "Sport estremi 🪂", "Enogastronomia 🍷", 
            "Relax e Spa 💆", "Tour in barca ⛵",
            "Safari e animali 🦁", "Festival e eventi 🎭"
        ]

        stile_check = """
            QCheckBox {
                color: white; font-size: 18px; font-weight: bold; spacing: 10px;
            }
            QCheckBox::indicator {
                width: 22px; height: 22px; border-radius: 5px;
                border: 2px solid white; background: rgba(255, 255, 255, 20);
            }
            QCheckBox::indicator:checked {
                background-color: #3498DB;
            }
        """

        for i, exp in enumerate(esperienze):
            cb = QCheckBox(exp)
            cb.setCursor(Qt.PointingHandCursor)
            cb.setStyleSheet(stile_check)
            cb.stateChanged.connect(self.gestisci_selezione)
            grid_esperienze.addWidget(cb, i // 2, i % 2)
            self.checks.append(cb)
        
        layout_corpo.addLayout(grid_esperienze)
        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; color: white; border: 2px solid white; 
                border-radius: 15px; font-weight: bold; font-size: 18px; 
            }
            QPushButton:hover { background-color: white; color: #000080; }
        """
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() 
        layout_nav.addWidget(btn_next)
        
        layout_principale.addLayout(layout_nav)

    def gestisci_selezione(self, state):
        checkbox = self.sender()
        if state == Qt.Checked:
            if len(self.scelta_esperienze) < 2:
                self.scelta_esperienze.append(checkbox.text())
            else:
                # Blocca la spunta se il limite è superato
                checkbox.blockSignals(True)
                checkbox.setChecked(False)
                checkbox.blockSignals(False)
                
                msg = QMessageBox(self)
                msg.setWindowTitle("Limite raggiunto")
                msg.setText("Puoi selezionare massimo 2 esperienze!")
                msg.setIcon(QMessageBox.Warning)
                msg.setStyleSheet("""
                    QMessageBox { background-color: #f0f0f0; }
                    QLabel { color: black; font-family: 'Arial'; font-size: 14px; qproperty-alignment: 'AlignCenter'; min-width: 250px; }
                    QPushButton { background-color: #e1e1e1; color: black; border: 1px solid #adadad; border-radius: 3px; width: 80px; height: 25px; }
                """)
                msg.exec_()
        else:
            if checkbox.text() in self.scelta_esperienze:
                self.scelta_esperienze.remove(checkbox.text())

# ====================== PAGINA 13: SICUREZZA ======================
class TredicesimaPagina(QWidget):
    def __init__(self, callback_indietro, callback_avanti):
        super().__init__()
        self.setStyleSheet("background: transparent;")

        layout_principale = QVBoxLayout(self)
        layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        layout_principale.addLayout(header_layout)

        layout_principale.addStretch(1)

        # --- CORPO CENTRALE ---
        corpo_centrale = QFrame()
        corpo_centrale.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 0, 0, 30); 
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 20);
            }
        """)
        layout_corpo = QVBoxLayout(corpo_centrale)
        layout_corpo.setContentsMargins(60, 50, 60, 50)
        layout_corpo.setSpacing(35)

        # Domanda Principale
        lbl_titolo = QLabel("Quanto è importante la sicurezza?")
        lbl_titolo.setAlignment(Qt.AlignCenter)
        lbl_titolo.setStyleSheet("color: white; font-size: 34px; font-weight: bold; background: none;")
        ombra_titolo = QGraphicsDropShadowEffect()
        ombra_titolo.setBlurRadius(20)
        ombra_titolo.setColor(QColor(0, 0, 128, 255))
        ombra_titolo.setOffset(3, 3)
        lbl_titolo.setGraphicsEffect(ombra_titolo)
        layout_corpo.addWidget(lbl_titolo)

        # Indicatore Livello 
        self.lbl_livello = QLabel("Sicurezza: Alta 🛡️")
        self.lbl_livello.setAlignment(Qt.AlignCenter)
        self.lbl_livello.setStyleSheet("color: #00FFCC; font-size: 26px; font-weight: bold;")
        layout_corpo.addWidget(self.lbl_livello)

        # Slider Sicurezza
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1, 5)
        self.slider.setValue(4)
        self.slider.setFixedWidth(450)
        self.slider.setCursor(Qt.PointingHandCursor)
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #bbb;
                height: 12px;
                background: white;
                border-radius: 6px;
            }
            QSlider::handle:horizontal {
                background: white;
                border: 3px solid #000080;
                width: 26px;
                height: 26px;
                margin: -8px 0;
                border-radius: 13px;
            }
            QSlider::sub-page:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FF4C4C, stop:0.5 #FFCC00, stop:1 #00FFCC);
                border-radius: 6px;
            }
        """)
        self.slider.valueChanged.connect(self.aggiorna_testo)
        layout_corpo.addWidget(self.slider, alignment=Qt.AlignCenter)

        # --- INFO SPOSTAMENTO ---
        lbl_info = QLabel("Sposta la barra per definire la tua priorità")
        lbl_info.setAlignment(Qt.AlignCenter)
        lbl_info.setStyleSheet("""
            color: rgb(0, 0, 128); 
            font-size: 18px; 
            font-weight: 600;
            font-style: italic;
            background-color: rgba(255, 255, 255, 0.5); 
        """)
        
        layout_corpo.addWidget(lbl_info, alignment=Qt.AlignCenter)

        layout_principale.addWidget(corpo_centrale, alignment=Qt.AlignCenter)
        layout_principale.addStretch(2)

        # --- NAVIGAZIONE  ---
        layout_nav = QHBoxLayout()
        layout_nav.setAlignment(Qt.AlignVCenter) 
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        btn_back = QPushButton("← Indietro")
        btn_next = QPushButton("Avanti →")
        
        btn_back.clicked.connect(callback_indietro)
        btn_next.clicked.connect(callback_avanti)
        
        style_nav = """
            QPushButton { 
                background-color: transparent; 
                color: white; 
                border: 2px solid white; 
                border-radius: 15px; 
                font-weight: bold; 
                font-size: 18px; 
            }
            QPushButton:hover { 
                background-color: white; 
                color: #000080; 
            }
        """
        
        for b in [btn_back, btn_next]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)
        
        layout_nav.addWidget(btn_back)
        layout_nav.addStretch() 
        layout_nav.addWidget(btn_next)
        
        layout_principale.addLayout(layout_nav)

    def aggiorna_testo(self, valore):
        livelli = {
            1: ("Bassa 🔓",    "#FF4C4C"),
            2: ("Moderata ⚠️", "#FFCC00"),
            3: ("Standard ✅", "#FFFFFF"),
            4: ("Alta 🛡️",     "#00FFCC"),
            5: ("Massima 👮",  "#00FF00")
        }
        testo, colore = livelli.get(valore)
        self.lbl_livello.setText(f"Sicurezza: {testo}")
        self.lbl_livello.setStyleSheet(f"color: {colore}; font-size: 26px; font-weight: bold;")
        
    def value(self):
        return self.slider.value()

# ====================== PAGINA RISULTATI ======================
class PaginaRisultati(QWidget):
    def __init__(self, callback_back=None, callback_home=None):
        super().__init__()
        self.callback_back = callback_back
        self.callback_home = callback_home
        self.layout_principale = QVBoxLayout(self)
        self.layout_principale.setContentsMargins(13, 13, 20, 50)

        # --- HEADER LOGO ---
        header_layout = QHBoxLayout()
        lbl_logo = QLabel("✈️ Novaroute")
        lbl_logo.setStyleSheet("color: white; font-size: 32px; font-weight: 800; letter-spacing: 2px;")
        ombra_logo = QGraphicsDropShadowEffect()
        ombra_logo.setBlurRadius(20)
        ombra_logo.setColor(QColor(0, 0, 128, 255))
        ombra_logo.setOffset(3, 3)
        lbl_logo.setGraphicsEffect(ombra_logo)
        header_layout.addWidget(lbl_logo)
        header_layout.addStretch()
        self.layout_principale.addLayout(header_layout)

        self.layout_principale.addStretch(1)
        
        # --- 2. TITOLO ---
        self.lbl_titolo = QLabel("")
        self.lbl_titolo.setAlignment(Qt.AlignCenter)
        self.lbl_titolo.setFixedHeight(65)
        self.lbl_titolo.setStyleSheet("""
            color: rgb(0, 0, 128); font-size: 24px; font-weight: 800; 
            background-color: rgba(255, 255, 255, 0.5); border: 2px solid #0096FF; border-radius: 15px;
        """)
        self.layout_principale.addWidget(self.lbl_titolo)

        self.layout_principale.addStretch(1)

        # --- 3. AREA PODIO ---
        self.layout_podio = QHBoxLayout()
        self.layout_podio.setAlignment(Qt.AlignCenter) 
        self.layout_podio.setSpacing(25)
        self.layout_principale.addLayout(self.layout_podio)

        self.layout_principale.addStretch(1)

        # --- 4. NAVIGAZIONE ---
        layout_nav = QHBoxLayout()
        layout_nav.setContentsMargins(30, 0, 30, 0)
        
        self.btn_back = QPushButton("← Indietro")
        self.btn_restart = QPushButton("Ricomincia →")
        
        self.btn_back.clicked.connect(self.callback_back)
        self.btn_restart.clicked.connect(self.callback_home)

        style_nav = """
            QPushButton { 
                background-color: transparent; color: white; border: 2px solid white; 
                border-radius: 15px; font-weight: bold; font-size: 18px; 
            }
            QPushButton:hover { background-color: white; color: #000080; }
        """
        
        for b in [self.btn_back, self.btn_restart]:
            b.setFixedSize(220, 65)
            b.setStyleSheet(style_nav)

        layout_nav.addWidget(self.btn_back)
        layout_nav.addStretch() 
        layout_nav.addWidget(self.btn_restart)
        
        self.layout_principale.addLayout(layout_nav)

    def pulisci_risultati(self):
        while self.layout_podio.count():
            item = self.layout_podio.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def crea_colonna(self, dati_meta, posizione):
        dest, score, percent, motivi = dati_meta
        colonna = QFrame()
        colore_vetro = "rgba(255, 255, 255, 130)"
        
        # Ridimensionamento altezze per effetto podio reale
        if posizione == 1: # ORO
            altezza = 490
            bordo = "4px solid #FFD700"
            medaglia = "🥇"
        elif posizione == 2: # ARGENTO
            altezza = 410
            bordo = "3px solid #C0C0C0"
            medaglia = "🥈"
        else: # BRONZO
            altezza = 350
            bordo = "3px solid #CD7F32"
            medaglia = "🥉"

        colonna.setFixedSize(290, altezza)
        colonna.setStyleSheet(f"QFrame {{ background-color: {colore_vetro}; border: {bordo}; border-radius: 30px; }}")

        layout_int = QVBoxLayout(colonna)
        layout_int.setContentsMargins(15, 20, 15, 20)
        
        stile_blu = "color: rgb(0, 0, 80); border: none; background: none;"

        lbl_nome = QLabel(f"{medaglia}\n{dest.nome}\n{dest.paese}")
        lbl_nome.setAlignment(Qt.AlignCenter)
        lbl_nome.setStyleSheet(f"font-size: 20px; font-weight: 900; {stile_blu}")
        lbl_nome.setWordWrap(True)
        
        lbl_stat = QLabel(f"🎯 Match: {percent}%\n⭐ Score: {score}")
        lbl_stat.setAlignment(Qt.AlignCenter)
        lbl_stat.setStyleSheet(f"font-size: 16px; font-weight: 700; border-bottom: 1px solid rgba(0,0,0,30); {stile_blu}")
        
        lbl_motivi = QLabel("💡 Perché:\n• " + "\n• ".join(motivi[:3]))
        lbl_motivi.setStyleSheet(f"font-size: 13px; font-weight: 600; {stile_blu}")
        lbl_motivi.setWordWrap(True)
        
        layout_int.addWidget(lbl_nome)
        layout_int.addWidget(lbl_stat)
        layout_int.addStretch()
        layout_int.addWidget(lbl_motivi)
        
        return colonna

    def mostra_risultato(self, risultati, nome):
        self.pulisci_risultati()
        self.lbl_titolo.setText(f"🌍 La meta perfetta per {nome}")

        if len(risultati) >= 3:
            # L'allineamento Qt.AlignBottom crea l'effetto scalino
            self.layout_podio.addWidget(self.crea_colonna(risultati[1], 2), alignment=Qt.AlignBottom)
            self.layout_podio.addWidget(self.crea_colonna(risultati[0], 1), alignment=Qt.AlignBottom)
            self.layout_podio.addWidget(self.crea_colonna(risultati[2], 3), alignment=Qt.AlignBottom)