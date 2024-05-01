create_country_table = '''
CREATE TABLE country(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150)
    );
'''

create_attori_table = '''
CREATE TABLE attori(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150)
    );
'''

create_director_table = '''
CREATE TABLE director(
    id INT AUTO_INCREMENT PRIMARY KEY ,
    name VARCHAR(150)
    );
'''

create_listed_in_table = '''
CREATE TABLE listed_in(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150)
    );
'''

create_show_table = '''
CREATE TABLE shows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150),
    duration VARCHAR(150),
    rating VARCHAR(150),
    description TEXT,
    date_added VARCHAR(20),
    release_year YEAR
    );
'''

create_dirige_table = '''
CREATE TABLE dirige(
    id_director INT,
    id_show INT,
    FOREIGN KEY (id_show) REFERENCES shows(id),
    FOREIGN KEY (id_director) REFERENCES director(id)
);
'''

create_partecipa_table = '''
CREATE TABLE partecipa(
    id_attori INT,
    id_show INT,
    FOREIGN KEY (id_show) REFERENCES shows(id),
    FOREIGN KEY (id_attori) REFERENCES attori(id)
);
'''

create_tratta_table = '''
CREATE TABLE tratta(
    id_listed_in INT,
    id_show INT,
    FOREIGN KEY (id_show) REFERENCES shows(id),
    FOREIGN KEY (id_listed_in) REFERENCES listed_in(id)
);
'''
create_partecipazione_paese_table = '''
CREATE TABLE partecipazione_paese(
    id_country INT,
    id_show INT,
    FOREIGN KEY (id_show) REFERENCES shows(id),
    FOREIGN KEY (id_country) REFERENCES country(id)
);
'''

