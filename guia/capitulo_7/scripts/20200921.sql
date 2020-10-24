sudo su postgres
psql

CREATE DATABASE capitulo_7_db;

CREATE USER capitulo_7_user WITH PASSWORD 'patata';

ALTER ROLE capitulo_7_user SET client_encoding TO 'utf8';
ALTER ROLE capitulo_7_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE capitulo_7_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE capitulo_7_db TO capitulo_7_user;

\c capitulo_7_db;

CREATE TABLE nota (
                    prioridad VARCHAR(10),
                    titulo VARCHAR(100),
                    contenido VARCHAR(200)
                    );

ALTER TABLE nota OWNER TO capitulo_7_user;

psql -U capitulo_7_user capitulo_7_db
