CREATE DATABASE capitulo_6_db;

CREATE USER capitulo_6_user WITH PASSWORD 'patata';

ALTER ROLE capitulo_6_user SET client_encoding TO 'utf8';
ALTER ROLE capitulo_6_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE capitulo_6_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE capitulo_6_db TO capitulo_6_user;

CREATE TABLE nota (
                    prioridad VARCHAR(10),
                    titulo VARCHAR(100),
                    contenido VARCHAR(200)
                    );

ALTER TABLE nota OWNER TO capitulo_6_user;

psql -U capitulo_6_user capitulo_6_db