# Definición de la lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Definir listas de magos y científicos
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]

# Crear función para hacer grandiosos a los magos
def hacer_grandioso(magos):
    return [f"El gran {mago}" for mago in magos]

# Crear función para imprimir nombres
def imprimir_nombres(lista_nombres):
    for nombre in lista_nombres:
        print(nombre)

# Filtrar los grupos de nombres
magos_grandiosos = hacer_grandioso(magos)
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

# Imprimir la lista original
print("Lista completa:")
imprimir_nombres(nombres)

# Imprimir los nombres de los magos grandiosos
print("\nMagos grandiosos:")
imprimir_nombres(magos_grandiosos)

# Imprimir los nombres de los científicos
print("\nCientíficos:")
imprimir_nombres(cientificos)

# Imprimir los nombres de los otros
print("\nOtros:")
imprimir_nombres(otros)
