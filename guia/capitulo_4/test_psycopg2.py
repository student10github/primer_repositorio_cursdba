import psycopg2
conn = psycopg2.connect(dbname="capitulo_4_db",
user="capitulo_4_user", password="patata")
print("Funciona!")