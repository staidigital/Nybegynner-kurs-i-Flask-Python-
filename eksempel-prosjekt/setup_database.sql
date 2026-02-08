-- =============================================
-- Flask-kurs: Oppsett av MariaDB-database
-- =============================================
-- Kjor denne filen for aa sette opp databasen:
--   mysql -u root -p < setup_database.sql
-- =============================================

-- Lag databasen (hvis den ikke finnes)
CREATE DATABASE IF NOT EXISTS flask_spilldb;

-- Bytt til databasen
USE flask_spilldb;

-- Lag tabellen for spillere
CREATE TABLE IF NOT EXISTS spillere (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(100) NOT NULL,
    favorittspill VARCHAR(200) NOT NULL
);

-- Legg til noen eksempel-data
INSERT INTO spillere (navn, favorittspill) VALUES
    ('Ola', 'Minecraft'),
    ('Kari', 'Fortnite'),
    ('Per', 'FIFA'),
    ('Lisa', 'The Legend of Zelda');

-- Vis innholdet i tabellen
SELECT * FROM spillere;
