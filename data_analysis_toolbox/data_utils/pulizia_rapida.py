import pandas as pd
import os

# 1. Trova la cartella dove si trova questo script (cioè data_utils)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Torna su di un livello e poi entra in 'data'
# '..' serve per uscire da data_utils e tornare nella radice
path_al_file = os.path.join(current_dir, "..", "data", "test.csv")

print(f"Sto cercando il file qui: {os.path.abspath(path_al_file)}")

if os.path.exists(path_al_file):
    df = pd.read_csv(path_al_file)
    print("✅ AGGANCIATO! Il file è pronto per il cleaning.")
    print(df.head())
else:
    print("❌ Errore: Il percorso non è corretto. Controlla i nomi delle cartelle.")
