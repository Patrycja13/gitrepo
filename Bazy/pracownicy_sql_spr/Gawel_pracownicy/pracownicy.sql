DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy (
    id_pracownika INTEGER PRIMARY KEY NOT NULL,
    imie TEXT(20) NOT NULL,
    nazwisko TEXT(20) NOT NULL,
    kod STRING(15),
    miasto_z TEXT(30),
    ulica TEXT(20),
    data_u DATE,
    miasto_u TEXT(30),
);


DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty (
    id_pracownika INTEGER PRIMARY KEY NOT NULL,
    typ_k TEXT(20) NOT NULL,
    kontakt STRING(15),
    uwagi TEXT(20)
    FOREIGN KEY(id_pracownika) REFERENCES pracownicy(id_pracownika)
    
);


DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska (
    id_stanowiska INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT(20),
);

    
    
DROP TABLE IF EXISTS place;
CREATE TABLE place (
    id_p INTEGER NOT NULL,
    id_s INTEGER NOT NULL,
    placa INTEGER,
    uwagi TEXT(20),
    data_z DATE,
    FOREIGN KEY(id_p) REFERENCES kontakty(id_pracownika),
    FOREIGN KEY(id_s) REFERENCES stanowiska(id_stanowiska),

);

    
