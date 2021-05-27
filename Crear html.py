include ':libs:twofish Python'
import webbrowser

#Cosas de cifrado
key = ')H&53,PMyCBuY[72C_Mc'
x = Twofish(b"""key""")
y = x.encrypt(b'tengoquetenercar')
Cifrado = str(y)
Descifrado = str(x.decrypt(y).decode())

#El html
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

with open('html_archivo.html', 'w') as f:
    f.write(str(html_archivo))
webbrowser.open("html_archivo.html")
