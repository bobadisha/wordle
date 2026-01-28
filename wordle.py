# Crear una palabra secreta
palabra_secreta = "hielo"
intentos = 0
maximo_intentos = 6
victoria = False

while intentos < maximo_intentos and not victoria :
    print(f"Intento {intentos + 1} de {maximo_intentos}")
    palabra = input("Ingrese una palabra de 5 letras")
    