import pandas as pd
import os
import sys

# Permette a Python di vedere i file nella stessa cartella
sys.path.append(os.path.dirname(__file__))

# IMPORTIAMO TUTTO
from cleaning_functions import (
    clean_column_names,
    check_missing_data,
    drop_empty_rows,
    fix_numeric_column,
)

# Percorso del file test.csv
base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, "..", "data", "test.csv")

if __name__ == "__main__":
    # Carichiamo i dati
    df = pd.read_csv(csv_path)

    # --- QUI LANCIAMO LE FUNZIONI NELL'ORDINE GIUSTO ---

    # 1. Puliamo le colonne (quella che avevi aggiunto)
    print("Colonne PRIMA della pulizia:", df.columns)

    # Lanciamo la funzione
    df = clean_column_names(df)

    print("Colonne DOPO la pulizia:", df.columns)
    print(f"tail di df dopo pulizia colonne {df.tail()}")
    # 2. Controlliamo i buchi (stampiamo il risultato per vederlo)
    print("Analisi iniziale NaN:")
    print(check_missing_data(df))

    # 3. Pulizia righe vuote
    df = drop_empty_rows(df)
    print(f"tail di df dopo  drop_empty_rows {df.tail()}")

    # 4. Sistemiamo la colonna prezzo (che è "sporca")
    df = fix_numeric_column(df, "prezzo")
    print(f"tail di df dopo  fix numeric columns {df.tail()}")

    # 5. Sistemiamo la colonna vendite
    df = fix_numeric_column(df, "vendite")
    print(f"tail di df dopo  fix numeric columns 2 {df.tail()}")

    # 6. Rimuoviamo i duplicati (se hai aggiunto la funzione)
    # df = remove_duplicates(df)

    print("\nEcco il risultato finale:")
    print(df.head(7))
