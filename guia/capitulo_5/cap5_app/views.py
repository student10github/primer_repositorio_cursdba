from django.shortcuts import render
from django.http import HttpResponse

import psycopg2

# Create your views here.

def insert(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emp VALUES ('7365','HUGO','OFICINISTA', \
                    '7903', DATE '1980-12-17','800.00',NULL,'20');")
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse("Insertado")

def select(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emp")
    html = '<html>'
    columns = [col[0] for col in cursor.description]
    for column in columns:
        html += str(column) + '|'
    html += '<br>'
    for empleado in cursor.fetchall():
        for columna in empleado:
            html += str(columna) + '|'
        html += '<br>'
    html += '</html>'
    cursor.close()
    conn.close()
    return HttpResponse(html)

def delect_all(request):
    conn = psycopg2.connect(dbname="capitulo_4_db",
                            user="capitulo_4_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("TRUNCATE TABLE emp;")
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse("Todos los registros han sido excluidos!")