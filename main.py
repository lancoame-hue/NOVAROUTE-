import sys # Modulo di sistema: necessario per gestire i parametri di chiusura dell'app
from PyQt5.QtWidgets import QApplication
from UI.main_window import FinestraPrincipale # Importazione finestra principale, gestisce il flusso di controllo e le impostazioni dell'app.

# 1. ISTANZA DELL'APPLICAZIONE, 'app' è un oggetto di tipo QApplication. 
# sys.argv è una lista di stringhe, senza questo oggetto non puoi creare finestre o gestire eventi (click, tasti).
app = QApplication(sys.argv)

# 2. CREAZIONE DELLA FINESTRA PRINCIPALE
# 'win' è un'istanza della tua classe FinestraPrincipale (tipo QStackedWidget) che inizializza tutti i widget, i layout e le pagine che hai definito nell'__init__.
win = FinestraPrincipale()

# 3. VISUALIZZAZIONE A SCHERMO INTERO
# Metodo: .showFullScreen() forza la finestra a coprire l'intera risoluzione del monitor.
win.showFullScreen()

# 4. CICLO DEGLI EVENTI E CHIUSURA PULITA
# app.exec_(): Avvia il "Main Loop" (un ciclo infinito che aspetta i click dell'utente).
# sys.exit(): Prende il codice di uscita dell'app (int) e lo passa al sistema operativo.
sys.exit(app.exec_())