import pandas as pd  # Per gestire i dati
import re  # Per usare le Regular Expressions (Regex)


def clean_column_names(df):
    """
    Standardize column names: lowercase, replace non-alphanumeric with
    a single underscore, and trim underscores from ends.
    """
    # 1. Create a copy to protect the original data
    df_clean = df.copy()
    new_columns = []

    for col in df_clean.columns:
        # 2. Lowercase first
        c = col.lower()

        # 3. Replace ANY non-alphanumeric block with ONE underscore
        # This handles spaces, symbols, and dots all at once
        c = re.sub(r"[^a-z0-9]+", "_", c)  # ^ è la negazione
        # [^a-z0-9] insieme significa: "Cerca qualsiasi cosa che NON sia una lettera o un numero"
        # +: Significa "uno o più". Se trova tre spazi di fila o un punto e una parentesi .(, li considera un unico blocco da sostituire.

        # 4. FINAL TOUCH: Strip underscores from the edges
        # This removes underscores created by symbols at the start or end
        c = c.strip("_")

        new_columns.append(c)

    # 5. Assign the clean list back to the dataframe
    df_clean.columns = new_columns
    return df_clean


def check_missing_data(df):
    """
    Mostra il conteggio dei valori mancanti per ogni colonna.
    È la fase di 'ispezione' fondamentale prima di agire.
    """
    missing_count = df.isnull().sum()
    print("--- Analisi buchi (NaN) ---")
    print(missing_count)
    return missing_count


def drop_empty_rows(df):
    """
    Rimuove le righe dove TUTTI i valori sono NaN.
    Utile per pulire file CSV che hanno righe vuote alla fine.
    """
    return df.dropna(how="all")


def fix_numeric_column(df, column_name):
    """
    Trasforma una colonna in numerica, convertendo gli errori o
    gli spazi vuoti in NaN, e poi mette 0.
    """
    # pd.to_numeric trasforma tutto in numeri.
    # errors='coerce' dice: "se trovi testo o spazi, trasformali in NaN"
    df[column_name] = pd.to_numeric(df[column_name], errors="coerce")

    # Ora che sono veri NaN, fillna(0) funzionerà!
    df[column_name] = df[column_name].fillna(0)
    return df
