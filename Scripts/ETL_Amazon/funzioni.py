from librerie import *
from librerie import pymongo


def connect_database():
    # Connessione al database MongoDB
    client = pymongo.MongoClient('mongodb+srv://johnjordanmack:Password@cluster0.iyh70dw.mongodb.net/')
    return client


def drop_database(client, nome_DB):
    # Elimina il database specificato
    client.drop_database(nome_DB)


def update_database(client, nome_DB, nome_collezione, dati_da_inserire):
    # Aggiorna il database inserendo i dati aggiornati
    try:
        db = client[nome_DB]
        collezione = db[nome_collezione]
        risultato = collezione.insert_many(dati_da_inserire)
        print(f"Inserimento avvenuto con successo. Documenti inseriti con ID: {risultato.inserted_ids}")
    except Exception as e:
        print("Errore durante l'inserimento:", e)



# Funzione per calcolare i sentiment con VADER per ogni recensione
def calculate_vader_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)

