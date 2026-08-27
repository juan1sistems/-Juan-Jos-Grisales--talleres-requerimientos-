import re

# Datos
palabras_vagas = ["rápido", "fácil", "bueno", "eficiente"]
palabras_imposibles = ["imposible", "perfectamente", "nunca"]
palabras_sistema = ["sistema", "usuario", "aplicación"]
palabras_verificables = ["registrar", "guardar", "mostrar", "enviar"]

# Pedir datos
identificador = input("Ingrese el identificador: ")
requisito = input("Ingrese el requisito: ")

requisito = requisito.lower()

print("\n--- RESULTADO ---")

# Específico
especifico = True

for palabra in palabras_vagas:
    if palabra in requisito:
        especifico = False

if especifico:
    print("Específico: SI")
else:
    print("Específico: NO")


# Medible
if re.search(r"\d+", requisito):
    print("Medible: SI")
else:
    print("Medible: NO")


# Alcanzable
alcanzable = True

for palabra in palabras_imposibles:
    if palabra in requisito:
        alcanzable = False

if alcanzable:
    print("Alcanzable: SI")
else:
    print("Alcanzable: NO")


# Relevante
relevante = False

for palabra in palabras_sistema:
    if palabra in requisito:
        relevante = True

if relevante:
    print("Relevante: SI")
else:
    print("Relevante: NO")


# Identificable
if identificador.startswith("REQ-"):
    print("Identificable: SI")
else:
    print("Identificable: NO")


# Verificable
verificable = False

for palabra in palabras_verificables:
    if palabra in requisito:
        verificable = True

if verificable:
    print("Verificable: SI")
else:
    print("Verificable: NO")
