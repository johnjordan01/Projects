#Importazione delle librerie
import csv
from funzioni import *
from query import *
import mysql.connector
from tqdm import tqdm

#Connessione al server MySQL, al database e creazione del DB
DB_Name = 'netflix'

connection = create_server_connection('localhost', 'root', '')
execute_query(connection, f'drop database if exists {DB_Name}')
create_database(connection, DB_Name)
connection = create_db_connection('localhost', 'root', '', DB_Name)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database= DB_Name
)
cursor = conn.cursor()


#Creazione tabelle
execute_query(connection, create_attori_table)
execute_query(connection, create_director_table)
execute_query(connection, create_listed_in_table)
execute_query(connection, create_show_table)
execute_query(connection, create_country_table)
execute_query(connection, create_partecipazione_paese_table)
execute_query(connection, create_partecipa_table)
execute_query(connection, create_dirige_table)
execute_query(connection, create_tratta_table)


#Lettura del file e trasformazioni
with open('netflix_data.csv', encoding='utf-8') as file:
    lettore = csv.reader(file)
    header = next(lettore)
    #print(header)

    lista_paesi = set()
    lista_attori = set()
    lista_direttori = set()
    lista_generi = set()
    lista_show = set()


    for riga in lettore:

        if riga[5] != '':
            for elem in riga[5].split(","):
                if elem.strip() != "":
                    lista_paesi.add(elem.strip())

        if riga[4] != '':
            for elem in riga[4].split(","):
                if elem.strip() != "":
                    lista_attori.add(elem.strip())

        if riga[3] != '':
            for elem in riga[3].split(","):
                if elem.strip() != "":
                    lista_direttori.add(elem.strip())

        if riga[10] != '':
            for elem in riga[10].split(","):
                if elem.strip() != "":
                    lista_generi.add(elem.strip())

        if riga[2]!= '':
            lista_show.add(riga[2])

        # Casting dei set in liste
        #lista_generi = list(lista_generi)
        #lista_direttori = list(lista_direttori)
        #lista_attori = list(lista_attori)
        #lista_paesi = list(lista_paesi)
        #lista_show = list(lista_show)


# Inserimento dei dati nel DB:

# relativi alla tabella country e creazione di un dizionario per memorizzare le Primary Keys
# avendo come chiavi i nomi dei paesi
diz_country = {}
x = 1
q1 = 'INSERT INTO country (id, name) VALUES (%s, %s)'
for paese in tqdm(lista_paesi):
    cursor.execute(q1, (x, paese))
    diz_country[paese] = x
    x += 1

# relativi alla tabella director e creazione di un dizionario per memorizzare le Primary Keys
diz_director = {}
x = 1
q2 = 'INSERT INTO director (id, name) VALUES (%s, %s)'
for direttore in tqdm(lista_direttori):
    cursor.execute(q2, (x, direttore))
    diz_director[direttore] = x
    x += 1

# relativi alla tabella attori e creazione di un dizionario per memorizzare le Primary Keys
diz_attori = {}
x = 1
q3 = 'INSERT INTO attori (id, name) VALUES (%s, %s)'
for attore in tqdm(lista_attori):
    cursor.execute(q3, (x, attore))
    diz_attori[attore] = x
    x += 1

# relativi alla tabella listed_in e creazione di un dizionario per memorizzare le Primary Keys
diz_generi = {}
x = 1
q4 = 'INSERT INTO listed_in (id, name) VALUES (%s, %s)'
for genere in tqdm(lista_generi):
    cursor.execute(q4, (x, genere))
    diz_generi[genere] = x
    x += 1


#conn.commit()


#Riapertura del file csv per inserimento dei dati relativi alle tabelle associative (NxN) nel DB
#grazie ai dizionari creati sopra
with open('netflix_data.csv', encoding='utf-8') as fichier:
    lettore = csv.reader(fichier)
    #header = next(lettore)


    q5 = 'INSERT INTO shows (id,title, duration, date_added, release_year, rating, description) VALUES (%s, %s, %s, %s, %s, %s, %s)'
 #   file.seek(0)  # Torna all'inizio del file
    next(lettore)
    diz_counter = 1
    diz_shows = {}

    for riga in tqdm(lettore):
        shows = riga[2].strip()
        duration = riga[9].strip()
        added = riga[6].strip()
        release = riga[7].strip()
        rating = riga[8].strip()
        description = riga[11].strip()
        title = shows.strip()
        cursor.execute(q5, (diz_counter, shows, duration, added, release, rating, description))
        diz_shows[title] = diz_counter
        diz_counter += 1
#conn.commit()


with open('netflix_data.csv', encoding='utf-8') as file:
    lettore=csv.reader(file)
    next(lettore)
    for riga in tqdm(lettore):
        if riga[10] != '':
            for elem in riga[10].split(","):
                if elem.strip() != "":
                    execute_query_place(conn,"INSERT INTO tratta (id_listed_in, id_show) VALUES (%s, %s)", (diz_generi[elem.strip()], diz_shows[riga[2].strip()]))

        if riga[3] != '':
            for elem in riga[3].split(","):
                if elem.strip() != "":
                    execute_query_place(conn,"INSERT INTO dirige (id_director, id_show) VALUES (%s, %s)", (diz_director[elem.strip()], diz_shows[riga[2].strip()]))

        if riga[4] != '':
            for elem in riga[4].split(","):
                if elem.strip() != "":
                    execute_query_place(conn,"INSERT INTO partecipa (id_attori, id_show) VALUES (%s, %s)", (diz_attori[elem.strip()], diz_shows[riga[2].strip()]))

        if riga[5] != '':
            for elem in riga[5].split(","):
                if elem.strip() != "":
                    execute_query_place(conn,"INSERT INTO partecipazione_paese (id_country, id_show) VALUES (%s, %s)", (diz_country[elem.strip()], diz_shows[riga[2].strip()]))
conn.commit()

#conn.close()