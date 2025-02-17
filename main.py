import requests

# URL del endpoint de GROBID
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

# Ruta del archivo PDF que quieres procesar
pdf_path = "2501.11091v1.pdf"

# Hacer la solicitud a GROBID
with open(pdf_path, "rb") as pdf_file:
    files = {"input": pdf_file}
    response = requests.post(GROBID_URL, files=files)

# Verificar la respuesta
if response.status_code == 200:
    print("Documento procesado con éxito!")
    print(response.text)  # Imprime el XML con el texto estructurado
else:
    print(f"Error en la solicitud: {response.status_code}")