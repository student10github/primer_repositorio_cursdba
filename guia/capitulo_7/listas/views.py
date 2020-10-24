import psycopg2.extras
import datetime, time

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def vista_principal(request):

    prioridad = request.GET.get('get_prioridad', default=None)

    with open("debug.log", "w") as debug_file:
        print(f"SELECT * FROM Nota WHERE prioridad LIKE '{prioridad}';", file=debug_file)

    conn = psycopg2.connect(dbname="capitulo_7_db",
                            user="capitulo_7_user",
                            password="patata")
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM Nota WHERE prioridad LIKE %s", (prioridad,))
#    cursor.execute(f"SELECT * FROM nota WHERE prioridad='{prioridad}';")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    params = {'notas': result}
    return render(request, 'home.html', params)


def anadir_page_view(request):
    return render(request, 'anadir.html')


def vista_anadir(request):
    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]

    conn = psycopg2.connect(dbname="capitulo_7_db",
                            user="capitulo_7_user",
                            password="patata")

    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]

    current_time = datetime.datetime.now()
    with open("debug.log", "a+") as debug_file:
        print(f"Registro {titulo} insertado a las {current_time}", file=debug_file)

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}','{titulo}','{nota}');")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('notas')