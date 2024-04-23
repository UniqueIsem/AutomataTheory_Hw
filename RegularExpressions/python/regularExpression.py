import re

def main():
    while True:
        print("M E N U")
        print("1. Ejemplo 1")
        print("2. Ejemplo 2")
        print("3. Salir")
        choice = input("Elige una opcion:")
        
        # EJEMPLO 1: Coincidir con un patrón específico en una cadena
        if choice == '1': 
            pattern = r'Python' #raw string
            text = input("Escribe algo, sabiendo que el patron es 'Python'")
            match = re.search(pattern, text)
            if match: # Si coinciden
                print('Coincidencia encontrada:', match.group())
            else:
                print('No se encontro coincidencia...')
        # Ejemplo 2: Buscar todas las coincidencias en una cadena
        elif choice == '2':
            pattern = r'\b\d{3}\b'  # Coincide con un número de 3 dígitos
            text = input("Escribe algo sabiendo que el patron es cualquier numero de 3 digitos (separado):")
            #text = 'Los números 123, 456 y 789 son ejemplos.'
            matches = re.findall(pattern, text)
            if matches: # Si coinciden
                print('Coincidencias encontradas:', matches)
            else:
                print('No se encontraron coincidencias...')
        elif choice == '3':
            print("Saliendo del sistema")
            break
        else:
            print("digite una opcion valida...")

if __name__ == "__main__":
    main()