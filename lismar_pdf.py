import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Conectar a la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="convertir_pdf"
)

conectar = db.cursor()

# Realizar una consulta a la base de datos
conectar.execute("SELECT titulo, descripcion FROM llenar_pdf")
data = conectar.fetchall()

# Generar un archivo PDF
pdf_filename = "datos.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)

y_position = 750  # Posición vertical para escribir en el PDF

for row in data:
    titulo, descripcion = row
    c.drawString(100, y_position, f"Título: {titulo}")
    c.drawString(100, y_position - 20, f"Descripción: {descripcion}")
    y_position -= 40  # Ajustar la posición vertical para el siguiente conjunto de datos

c.save()

print(f"Archivo PDF '{pdf_filename}' generado exitosamente.")



