# Moduli standard di PyQt5 per l'interfaccia grafica
from PyQt5.QtWidgets import QStackedWidget, QMessageBox # QStackedWidget: contenitore a pagine; QMessageBox: finestre di avviso.
from PyQt5.QtCore import Qt # Contiene costanti fondamentali di Qt (es. i tasti come Qt.Key_Escape).

# Importazione della logica applicativa e delle componenti UI personalizzate
from core.algoritmo import calcola_meta_perfecta # Importa la funzione che processa i dati e restituisce i match.
from UI.pages import * # Importa tutte le classi delle singole pagine
import os # Modulo di sistema per la gestione dei file, utilizzato per manipolare i percorsi dei file (es. caricamento dinamico dello sfondo).

class FinestraPrincipale(QStackedWidget):
    def __init__(self):
        super().__init__()

        # Recupera il percorso assoluto della cartella del progetto (tipo: str).
        BASE = os.path.dirname(os.path.abspath(__file__))
        # Crea il percorso dell'immagine normalizzando gli slash per il CSS (tipo: str).
        percorso = os.path.join(BASE, "sfondo_app.png").replace("\\", "/")
        #Applica l'immagine come sfondo adattabile a tutto il widget (metodo: setStyleSheet).
        self.setStyleSheet(f"""FinestraPrincipale {{border-image: url('{percorso}') 0 0 0 0 stretch stretch;}}""")

        # Inizializza le pagine (oggetti QWidget) passando le funzioni di navigazione come callback.
        self.pag1 = PaginaIniziale(self.vai_a_pag2)
        self.pag2 = SecondaPagina(self.vai_a_pag1, self.vai_a_pag3)
        self.pag3 = TerzaPagina(self.vai_a_pag2, self.vai_a_pag4)
        self.pag4 = QuartaPagina(self.vai_a_pag3, self.vai_a_pag5)
        self.pag5 = QuintaPagina(self.vai_a_pag4, self.vai_a_pag6)
        self.pag6 = SestaPagina(self.vai_a_pag5, self.vai_a_pag7)
        self.pag7 = SettimaPagina(self.vai_a_pag6, self.vai_a_pag8)
        self.pag8 = OttavaPagina(self.vai_a_pag7, self.vai_a_pag9)
        self.pag9 = NonaPagina(self.vai_a_pag8, self.vai_a_pag10)
        self.pag10 = DecimaPagina(self.vai_a_pag9, self.vai_a_pag11)
        self.pag11 = UndicesimaPagina(self.vai_a_pag10, self.vai_a_pag12)
        self.pag12 = DodicesimaPagina(self.vai_a_pag11, self.vai_a_pag13)
        self.pag_sicurezza = TredicesimaPagina(self.vai_a_pag12, self.vai_a_risultato)
        self.pag13 = PaginaRisultati(self.vai_a_pag_sicurezza_back, self.vai_a_pag1)

        # Inserisce tutti gli oggetti pagina in una lista per l'aggiunta allo stack.
        pagine = [
            self.pag1, self.pag2, self.pag3, self.pag4,
            self.pag5, self.pag6, self.pag7, self.pag8,
            self.pag9, self.pag10, self.pag11, self.pag12,
            self.pag_sicurezza, self.pag13
        ]
        # Aggiunge i widget allo stack; l'ordine determina l'indice numerico (metodo: addWidget).
        for p in pagine:
            self.addWidget(p)

        # Visualizza la prima pagina (indice 0) all'apertura dell'applicazione.
        self.setCurrentIndex(0)

     # ====================== NAVIGAZIONE ======================
    def vai_a_pag1(self):
        # Riporta la visualizzazione all'indice 0 dello stack (Pagina Iniziale).
        self.setCurrentIndex(0)

    def vai_a_pag2(self):
        # Sposta la visualizzazione all'indice 1 (Seconda Pagina).
        self.setCurrentIndex(1)

    def vai_a_pag3(self):
        # Recupera l'input nome (str) e rimuove spazi vuoti con .strip().
        nome = self.pag2.input_nome.text().strip()
        # Se la stringa è vuota, blocca il passaggio con un avviso (QMessageBox).
        if not nome:
            QMessageBox.warning(self, "Attenzione", "Per favore, inserisci il tuo nome!")
            return
        # Imposta il nome dell'utente nel saluto della pagina successiva.
        self.pag3.aggiorna_nome(nome)
        self.setCurrentIndex(2)

    def vai_a_pag4(self):
        # Procede all'indice 3 del QStackedWidget.
        self.setCurrentIndex(3)

    def vai_a_pag5(self):
        # Procede all'indice 4 del QStackedWidget.
        self.setCurrentIndex(4)

    def vai_a_pag6(self):
        # Verifica che l'attributo scelta_stagione (str) non sia vuoto o nullo.
        if not self.pag5.scelta_stagione:
            QMessageBox.warning(self, "Attenzione", "Seleziona una stagione!")
            return
        self.setCurrentIndex(5)

    def vai_a_pag7(self):
        # Recupera il testo dell'input (str) per la durata del viaggio.
        valore = self.pag6.input_giorni.text().strip()
        if not valore:
            QMessageBox.warning(self, "Attenzione", "Inserisci un numero di giorni!")
            return
        try:
            # Tenta la conversione in intero (int) per validare il dato numerico.
            giorni = int(valore)
        except ValueError:
            # Gestisce l'errore nel caso l'utente inserisca caratteri non numerici.
            QMessageBox.warning(self, "Attenzione", "Inserisci un numero valido!")
            return
        # Controlla che il numero sia compreso nel range logico consentito.
        if giorni < 1 or giorni > 365:
            QMessageBox.warning(self, "Attenzione", "I giorni devono essere tra 1 e 365!")
            return
        self.setCurrentIndex(6)

    def vai_a_pag8(self):
        # Passa all'indice 7 dello stack.
        self.setCurrentIndex(7)

    def vai_a_pag9(self):
        # Controlla la presenza di una selezione climatica salvata come stringa.
        if not self.pag8.scelta_clima:
            QMessageBox.warning(self, "Attenzione", "Seleziona un tipo di clima!")
            return
        self.setCurrentIndex(8)

    def vai_a_pag10(self):
        # Verifica se è stata fatta una scelta geografica.
        if not self.pag9.scelta_regione:
            QMessageBox.warning(self, "Attenzione", "Seleziona un paese!")
            return
        self.setCurrentIndex(9)

    def vai_a_pag11(self):
        # Valida la selezione dell'attributo paesaggio (str) prima di proseguire.
        if not self.pag10.scelta_paesaggio:
            QMessageBox.warning(self, "Attenzione", "Scegli un paesaggio!")
            return
        self.setCurrentIndex(10)

    def vai_a_pag12(self):
        # Verifica se l'utente ha selezionato il mood (str) nella pagina 11.
        if not self.pag11.scelta_mood:
            QMessageBox.warning(self, "Attenzione", "Seleziona un mood!")
            return
        self.setCurrentIndex(11)

    def vai_a_pag13(self):
        # Inizializza una lista vuota per raccogliere le checkbox selezionate.
        scelte = []
        # Itera sulla lista di oggetti QCheckBox della pagina 12.
        for cb in self.pag12.checks:
            # Aggiunge l'oggetto alla lista se il metodo .isChecked() è True.
            if cb.isChecked():
                scelte.append(cb)        
        # Blocca se la lista risultante è vuota (nessuna esperienza scelta).
        if not scelte:
            QMessageBox.warning(self, "Attenzione", "Seleziona almeno un'esperienza!")
            return
        self.setCurrentIndex(12)

    def vai_a_risultato(self):
        # Richiama l'algoritmo di matching passando l'intera istanza della finestra.
        top3 = calcola_meta_perfecta(self)
        # Passa i risultati elaborati (list) e il nome alla PaginaRisultati.
        self.pag13.mostra_risultato(top3, self.pag2.input_nome.text())
        self.setCurrentIndex(13)

    def vai_a_pag_sicurezza_back(self):
        # Funzione di ritorno specifica per tornare alla pagina di conferma.
        self.setCurrentIndex(12)

    def keyPressEvent(self, event):
        # Rileva eventi tastiera: se viene premuto ESC, esce dal FullScreen.
        # 'event' è un oggetto QKeyEvent che contiene il codice del tasto.
        if event.key() == Qt.Key_Escape:
            self.showNormal()