import psycopg2.extras
import datetime, time

from io import BytesIO

from reportlab.pdfgen import canvas
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

# Create your views here.

def home_page_view(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
#    cursor = conn.cursor()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM nota;")
#    result = cursor.fetchone()
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

    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
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
    return redirect('/home/')


def hello_pdf_antigo(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    p = canvas.Canvas(response)

    p.drawString(100, 100, "Hello world.")

    p.showPage()
    p.save()
    return response



def hello_pdf(request):

    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM nota;")

#    result = cursor.fetchall()
#    cursor.close()
#    conn.close()
#    params = {'notas': result}

    print
    "Genero el PDF"
    response = HttpResponse(content_type='application/pdf')
    pdf_name = "render_pdf.pdf"  # llamado clientes
    # la linea siguiente es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Notas", styles['Heading1'])
    clientes.append(header)
    headings = ('Prioridad', 'Titulo', 'Texto')
    allclientes = [(nota['prioridad'], nota['titulo'], nota['contenido']) for nota in cursor.fetchall()]

    with open('Debug.log', 'a+') as debug:
        print(allclientes, file=debug)

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()

    cursor.close()
    conn.close()

    return response