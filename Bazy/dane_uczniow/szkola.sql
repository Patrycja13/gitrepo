DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska (
    nr_ucznia INTEGER PRIMARY KEY NOT NULL,
    nazwisko TEXT(20) NOT NULL,
    imie1 TEXT(20) NOT NULL,
    imie2 TEXT(20)

);

DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe (
    nr_ucznia INTEGER,
    dzien INTEGER,
    miesiac INTEGER,
    rok INTEGER,
    miejsce_ur TEXT(20) DEFAULT "Gdańsku",
    wojewodztwo TEXT(20) DEFAULT "pomorskie",
    FOREIGN KEY (nr_ucznia) REFERENCES nazwiska(nr_ucznia)


);

DROP TABLE IF EXISTS oceny;
CREATE TABLE OCENY (
    nr_ucznia INTEGER,
    zach DECIMAL,
    rel DECIMAL DEFAULT NULL,
    pol DECIMAL,
    ang DECIMAL,
    niem DECIMAL,
    mat DECIMAL,
    his DECIMAL,
    geo DECIMAL,
    biol DECIMAL,
    fiz DECIMAL,
    chem DECIMAL,
    tech DECIMAL,
    info DECIMAL DEFAULT NULL,
    plas DECIMAL,
    PO DECIMAL,
    WF DECIMAL DEFAULT NULL,

    
    FOREIGN KEY (nr_ucznia) REFERENCES nazwiska(nr_ucznia)


);

INSERT INTO nazwiska(nr_ucznia, nazwisko, imie1, imie2)
VALUES (9201,"Adamczuk","Agata","");
INSERT INTO nazwiska
VALUES (9802,"Adamiuk","Marta","");


-- aby dodać dane do tabeli uzywamy INSERT
-- VALUES - wartości

-- w terminalu : 
-- sqlite3 baza.db < szkola.sql
-- sqlite3 baza.db
-- .table
-- .schema
-- .quit
-- NOT NULL - w polach, które sa obowiązkowe
-- DEFAULT NULL - domyślnie, wstawianie "nic'
