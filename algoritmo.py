from core.database import crea_database

def raccogli_risposte_utente(main_win):
        
        """Estrae i dati dai widget della UI e li organizza in un dizionario."""

        esperienze = []
        for cb in main_win.pag12.checks:
            if cb.isChecked():
                esperienze.append(cb.text())

        return {
            'nome':              main_win.pag2.input_nome.text().strip(),       # (str) Nome utente pulito.
            'giorni':            int(main_win.pag6.input_giorni.text()),        # (int) Durata del viaggio.
            'budget_max':        main_win.pag4.slider.value(),                  # (int) Valore numerico dello slider.
            'stagione':          main_win.pag5.scelta_stagione,                 # (str) Stagione scelta.
            'num_persone':       main_win.pag7.spin_total.value(),              # (int) Valore da QSpinBox.
            'num_bambini':       main_win.pag7.spin_bambini.value(),            # (int) Valore da QSpinBox.
            'disabilita':        main_win.pag7.check_disabilita.isChecked(),    # (bool) Stato checkbox.
            'clima':             main_win.pag8.scelta_clima,                    # (str) Clima scelto.
            'regione':           main_win.pag9.scelta_regione,                  # (str) Europa o Mondo.
            'paesaggio':         main_win.pag10.scelta_paesaggio,               # (list/str) Preferenze ambientali.
            'mood':              main_win.pag11.scelta_mood,                    # (list/str) Stato d'animo scelto.
            'esperienze':        esperienze, # (list) Testi dei checkbox attivi.
            'sicurezza_priorita':main_win.pag_sicurezza.value(),                # (int) Peso dato alla sicurezza (1-10).
        }

def calcola_meta_perfecta(main_win):
        
        """ Algoritmo Core: confronta le risposte con il database e calcola i punteggi."""

        dati = raccogli_risposte_utente(main_win)   # (dict) Input utente.
        destinazioni = crea_database()              # (list) Lista di oggetti 'Destinazione'.
        risultati = []                              # (list) Conterrà tuple (dest, score, motivi).

        def pulisci(testo): # "Montàgna!!" → "montagna"
            
            """Normalizza le stringhe per il confronto (lowercase, no accenti, no simboli)."""

            if not testo: # se è vuoto ritorno una stringa vuota
                return ""
            testo = str(testo).lower() # se no converte in stringa e in minuscolo
            # Sostituzione manuale caratteri speciali per evitare problemi di codifica.
            testo = testo.replace("à", "a").replace("è", "e").replace("é", "e")
            testo = testo.replace("ì", "i").replace("ò", "o").replace("ù", "u")
            risultato_pulito = ""
            for carattere in testo:
                if carattere.isalnum(): # Filtra tenendo solo lettere e numeri.
                    risultato_pulito += carattere
            return risultato_pulito

        # --- CICLO DESTINAZIONI ---
        for dest in destinazioni: # Itera su ogni oggetto meta nel database.
            score = 0             # (int) Punteggio accumulato per la meta corrente.
            motivi = []           # (list) Stringhe che spiegano perché la meta è consigliata.

            # 1. FILTRO CONTINENTE (Logica booleana)
            regione_u = dati['regione'].lower()
            cont_d = dest.continente.lower()
            
            # Se la regione scelta non coincide con quella della meta, scarta la meta (continue).
            if regione_u == "europa" and cont_d != "europa":
                continue
            if regione_u == "mondo" and cont_d == "europa":
                continue

            # 2. BUDGET (Calcolo matematico)
            giorni = dati['giorni']
            if giorni < 1: # Evita divisione per 0
                giorni = 1
            
            # Calcola quanto l'utente può spendere al giorno (tipo float).
            budget_giornaliero_utente = dati['budget_max'] / giorni
            
            # Confronto tra budget utente e costo medio giornaliero della meta.
            if budget_giornaliero_utente >= dest.budget:
                score += 50
                motivi.append("💰 Budget perfetto")
            elif budget_giornaliero_utente >= (dest.budget * 0.7): # Se l’utente ha almeno il 70% del budget richiesto
                score += 20
                motivi.append("💰 Budget al limite")
            else:
                score = score - 30 # Penalità se troppo costosa.

            # 3. STAGIONE E CLIMA (Confronto stringhe normalizzate)
            if pulisci(dati['stagione']) == pulisci(dest.stagione) or pulisci(dest.stagione) == "tuttolanno":
                score += 40
                motivi.append("🌤️ Periodo ideale")
            
            if pulisci(dati['clima']) == pulisci(dest.clima):
                score += 30
                motivi.append("🌡️ Clima preferito")

            # 4. PAESAGGIO 
            match_paesaggio = False
            for p in dati['paesaggio']:
                for dp in dest.paesaggio:
                    if pulisci(p) == pulisci(dp):
                        match_paesaggio = True
            
            if match_paesaggio == True:
                score += 40
                motivi.append("🏞️ Paesaggio trovato")

            # 5. MOOD
            match_mood = False
            for m in dati['mood']:
                for dm in dest.mood:
                    if pulisci(m) == pulisci(dm):
                        match_mood = True
            
            if match_mood == True:
                score += 40
                motivi.append("💫 Mood azzeccato")

            # 6. SICUREZZA - moltiplica il valore della meta (1-10) per la priorità dell'utente (1-10).
            punti_sicurezza = dest.sicurezza * dati['sicurezza_priorita']
            score += punti_sicurezza

            # 7. FAMIGLIA E DISABILITÀ (Check booleani)
            if dati['num_bambini'] > 0 and dest.famiglia == True:
                score += 25
            if dati['disabilita'] == True and dest.disabilita == True:
                score += 25

            # Salva la meta elaborata con il suo punteggio e i motivi trovati.
            risultati.append((dest, score, motivi))

        # --- ORDINAMENTO (Metodo, sort) ---
        # (dest, score, motivi) -> ("Roma", 120, ["Budget perfetto", "Clima ideale"])

        def prendi_punteggio(elemento):
            # Funzione chiave per estrarre lo score (indice 1 della tupla).
            return elemento[1] 
        
        # Ordina la lista in modo decrescente (reverse=True) in base allo score, usa come criterio (key) la funzione prendi_punteggio
        risultati.sort(key=prendi_punteggio, reverse=True)

        # --- CREAZIONE TOP 3 FINALE ---
        top3 = [] # (list) Conterrà solo i primi 3 risultati formattati, ma con min se sono meno di 3 non crasha.
        for i in range(min(3, len(risultati))):
            d, s, m = risultati[i] # (dest, score, motivi)
            # Calcolo percentuale di affinità (normalizzata tra 0 e 100), 350 punteggio massimo teorico.
            percentuale = int((s / 350) * 100)
            if percentuale > 100: 
                percentuale = 100
            if percentuale < 0: 
                percentuale = 0
            
            # Salva la tupla finale con la percentuale pronta per la PaginaRisultati.
            top3.append((d, s, percentuale, m))

        return top3