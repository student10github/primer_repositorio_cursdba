sudo su postgres

psql

CREATE DATABASE m2uf3;

\c m2uf3;

CREATE USER m2uf3_user WITH PASSWORD 'patata';

ALTER ROLE m2uf3_user SET client_encoding TO 'utf8';
ALTER ROLE m2uf3_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE m2uf3_user SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE m2uf3 TO m2uf3_user;

CREATE TABLE emp (
                  empnum decimal(4,0) NOT NULL,
                  enombre varchar(30) default NULL,
                  sal decimal(7,2) default NULL,
                  puesto varchar(15) default NULL
                  );

\dt

ALTER TABLE emp OWNER TO m2uf3_user;

psql -U m2uf3_user m2uf3

\d emp