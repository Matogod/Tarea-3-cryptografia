from twofish import Twofish
import webbrowser

#Ingresar clave de cifrado
key = input('Ingrese una clave para cifrar: ')
#Ejemplo: )H&53,PMyCBuY[72C_Mc
x = Twofish(b"""key""")
#Mensaje cifrado: 
y = x.encrypt(b"mimamamemimamama")
Cifrado = str(y)

#Crear el html
html_archivo = """<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="URF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="wodth=device-width, initial-scale=1.0">
        <title>Tarea 3 Crypto</title>
    </head>
    <body>
        <p>Este sitio contiene un mensaje secreto</p>
        <div class="twofish" id="""+Cifrado+"""></div>
        <div class="key" id="""+key+"""></div>
    </body>
</html>
"""
#Crea el archivo .html y lo abre
with open('html_archivo.html', 'w') as f:
    f.write(str(html_archivo))
webbrowser.open("html_archivo.html")
