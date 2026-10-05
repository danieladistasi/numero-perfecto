numeros = []

print("--- ETAPA 1: Crear la lista ---")
while True:
    # Pedimos el número al usuario
    numero = int(input("Ingresa un número entero positivo (o uno no-positivo para terminar): "))
    
    # Si es 0 o negativo, terminamos de pedir números
    if numero <= 0:
        break
    
    # Si es positivo, lo agregamos a la lista
    numeros.append(numero)

# Imprimimos la lista como pide el problema
print("\nLa lista final es:", numeros)

print("\n--- ETAPA 2: Buscar elementos ---")
while True:
    # Pedimos la posición (índice 1 en adelante)
    posicion = int(input("Ingresa la posición que quieres ver (entero positivo, o uno no-positivo para salir): "))
    
    # Si ingresa 0 o negativo, el programa termina
    if posicion <= 0:
        print("Programa terminado.")
        break
    
    # Le restamos 1 porque en Python las listas empiezan a contar desde el índice 0
    indice = posicion - 1
    
    # Verificamos que la posición exista dentro de la lista
    if indice < len(numeros):
        print(f"El elemento en la posición {posicion} es: {numeros[indice]}")
    else:
        print(f"Error: La lista solo tiene {len(numeros)} elementos. Intenta con una posición menor.")