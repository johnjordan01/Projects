from librerie import *
from funzioni import *


# Inizializzazione delle liste e variabili
recensioni = []
dati_da_inserire = []



# Lettura del file CSV e elaborazione dei dati
with open('amazon.csv', encoding='utf-8') as file:
    lettore = csv.DictReader(file)
    for riga in tqdm(lettore):
        # Estrazione dei dati necessari dal CSV
        user_id = riga['user_id'].split(',')
        user_name = riga['user_name'].split(',')
        review_id = riga['review_id'].split(',')
        review_title = riga['review_title'].split(',', maxsplit=len(user_id))
        review_content = riga['review_content'].split(',', maxsplit=len(user_id))
        prodotto = riga['product_id']
        categorie = riga['category'].split('|')
        description = riga['about_product']


        #conversione dei valori della colonna [discounted_price] da rupie in euro
        try:
            rupie_strip = float(riga['discounted_price'].strip('₹').replace(',', ''))
        except ValueError:
            rupie_strip = 0.0

        converter = CurrencyRates()
        convertion_discounted = converter.convert('INR', 'EUR', rupie_strip)


        #conversione dei valori della colonna [actual_price] da rupie in euro
        try:
            actual_price = float(riga['actual_price'].strip('₹').replace(',', ''))
        except ValueError:
            actual_price = 0.0

        convertion_actual_price = converter.convert('INR', 'EUR', actual_price)


        #Trasformazione dei valori della colonna [rating_count] in un formato adeguato
        try:
            rating_count = int(riga['rating_count'].replace(',', ''))
            if rating_count > 999:
                format_rating_count = "{:,}".format(rating_count)
            else:
                format_rating_count = str(rating_count)
        except ValueError:
            format_rating_count = '0'


        for id, name, review, title, content in zip(user_id, user_name, review_id, review_title, review_content):
            # Calcolo dei sentiment con VADER e Roberta per ogni recensione
            vader_result = calculate_vader_sentiment(content)

            recensione = {
                "user_id": id,
                "user_name": name,
                "review": {
                    "review_id": review,
                    "review_title": title,
                    "review_content": content,
                    "sentiment_vader": vader_result,
                }
            }
            recensioni.append(recensione)

        documento = {
            'id': prodotto,
            'category': categorie,
            'discount_price': convertion_discounted,
            'actual_price': convertion_actual_price,
            'rating_count': rating_count,
            'description': description,
            'review': recensioni
        }
        dati_da_inserire.append(documento)



# Connessione al database
client = connect_database()
nome_DB = "Amazon"
nome_collezione = "prodotti"


# Opzione per cancellare o aggiornare il database
scelta = input("Vuoi cancellare il database (C) o aggiornarlo (A)? ").upper()

if scelta == "C":
    drop_database(client, nome_DB)
    print("Database eliminato con successo!")
elif scelta == "A":
    update_database(client, nome_DB, nome_collezione, dati_da_inserire)
    print("Database aggiornato con successo!")
else:
    print("Opzione non valida. Non è stato fatto nulla.")

# Chiusura della connessione al database
client.close()


