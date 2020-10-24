import psycopg2
import datetime

from django.shortcuts import render, redirect

# Create your views here.
def nuevo_empleado_page_view(request):
    return render(request, 'nuevo_empleado.html')

def vista_anadir(request):

    conn = psycopg2.connect(dbname="m2uf3",
                            user="m2uf3_user",
                            password="patata")

    empnum = request.POST["empnum"]
    enombre = request.POST["enombre"]
    sal = request.POST["sal"]
    puesto = request.POST["puesto"]

    current_time = datetime.datetime.now()
    with open("debug.log", "a+") as debug_file:
        print(f"Registro {empnum} insertado a las {current_time}", file=debug_file)

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO emp VALUES ('{empnum}','{enombre}','{sal}','{puesto}');")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('vista_anadida')

def vista_anadida(request):
    return render(request, 'anadido.html')