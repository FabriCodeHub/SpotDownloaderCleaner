# SpotDownloaderCleaner

SpotDownloaderCleaner è uno script Python progettato per rimuovere la stringa `[SPOTDOWNLOADER.COM]` dai titoli dei tag ID3 dei file MP3. Inoltre, può rinominare i file stessi rimuovendo la stessa stringa dal nome del file.

## Requisiti

- Python 3.x
- Libreria `mutagen` (per la gestione dei tag ID3)

## Installazione

1. Assicurati di avere Python 3 installato sul tuo sistema.
2. Installa la libreria `mutagen` eseguendo il seguente comando:

   ```bash
   pip install mutagen

Clona questo repository o scarica lo script SpotDownloaderCleaner.py.

Utilizzo
Modifica lo script SpotDownloaderCleaner.py inserendo il percorso della tua installazione di Python e il percorso della cartella contenente i file MP3.

python
Copy
sys.path.append(r"INSERISCI IL PERCORSO DELLA TUA INSTALLAZIONE DI PYTHON")
cartella_canzoni = r"INSERISCI IL PERCORSO DEL SALVATAGGIO DELLE CANZONI"
Esegui lo script:

bash
Copy
python SpotDownloaderCleaner.py
Lo script rimuoverà la stringa [SPOTDOWNLOADER.COM] dai titoli dei tag ID3 e, se specificato, rinominerà i file rimuovendo la stessa stringa.

Parametri
cartella: Percorso della cartella contenente i file MP3.

stringa_da_rimuovere: Stringa da rimuovere dai titoli e, opzionalmente, dai nomi dei file (di default è [SPOTDOWNLOADER.COM]).

rinomina_file: Se True, rinomina i file rimuovendo la stringa specificata. Se False, modifica solo i tag ID3.

Esempio
Supponiamo di avere una cartella con i seguenti file MP3:

Canzone1 [SPOTDOWNLOADER.COM].mp3
Canzone2 [SPOTDOWNLOADER.COM].mp3

Eseguendo lo script con stringa_da_rimuovere = "[SPOTDOWNLOADER.COM]" e rinomina_file = True, i file verranno modificati come segue:

I titoli dei tag ID3 saranno puliti, rimuovendo [SPOTDOWNLOADER.COM].

I file verranno rinominati in Canzone1.mp3 e Canzone2.mp3.
