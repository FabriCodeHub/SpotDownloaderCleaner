#!/usr/bin/env python3
import os
import sys
sys.path.append(r"INSERISCI IL PERCORSO DELLA TUA INSTALLAZIONE DI PYTHON")
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

def pulisci_titoli(cartella, stringa_da_rimuovere, rinomina_file=False):
    for filename in os.listdir(cartella):
        if not filename.lower().endswith(".mp3"):
            continue
        file_path = os.path.join(cartella, filename)
        try:
            # Carica i tag esistenti o creali se non presenti
            audio = EasyID3(file_path)
        except ID3NoHeaderError:
            audio = EasyID3()
            audio.save(file_path)
            audio = EasyID3(file_path)
        except Exception as e:
            print(f"Errore nell'aprire {filename}: {e}")
            continue

        if not audio.get('title'):
            print(f"Nessun tag 'title' in {filename}. Saltato.")
            continue

        titolo_originale = audio['title'][0]
        nuovo_titolo = titolo_originale.replace(stringa_da_rimuovere, "").lstrip(" .").strip()
        if not nuovo_titolo:
            print(f"Titolo vuoto dopo pulizia in {filename}. Saltato.")
            continue

        audio['title'] = nuovo_titolo
        try:
            audio.save()
            print(f"Modificato tag: {titolo_originale} → {nuovo_titolo}")
        except Exception as e:
            print(f"Errore nel salvare {filename}: {e}")

        # Se si desidera rinominare anche il file, rimuovi la stringa dal nome
        if rinomina_file:
            nuovo_nome = filename.replace(stringa_da_rimuovere, "").lstrip(" .").strip()
            # Assicurati che il nuovo nome termini con .mp3
            if not nuovo_nome.lower().endswith(".mp3"):
                nuovo_nome += ".mp3"
            nuovo_file_path = os.path.join(cartella, nuovo_nome)
            try:
                os.rename(file_path, nuovo_file_path)
                print(f"Rinominato file: {filename} → {nuovo_nome}")
            except Exception as e:
                print(f"Errore nel rinominare {filename}: {e}")

    print("Pulizia completata.")

if __name__ == '__main__':
    # Specifica il percorso della cartella contenente i file MP3
    cartella_canzoni = r"INSERISCI IL PERCORSO DEL SALVATAGGIO DELLE CANZONI"
    stringa_da_rimuovere = "[SPOTDOWNLOADER.COM]"
    # Imposta a True se vuoi rinominare anche il file, False se vuoi solo aggiornare i tag
    pulisci_titoli(cartella_canzoni, stringa_da_rimuovere, rinomina_file=True)
