def intersection(l1, l2):
    return set(l1) & set(l2)

def difference(l1, l2):
    return set(l1) - set(l2)

def concatenation(l1, l2):
    result = set()
    for word1 in l1:
        for word2 in l2:
            result.add(word1 + word2)
    return result

def prefixes(word):
    result = set()
    for i in range(len(word)+1):
        result.add(word[:i])
    return result

def suffixes(word):
    result = set()
    for i in range(len(word)+1):
        result.add(word[i:])
    return result

def main():
    l1 = []
    num_words_l1 = int(input("¿Cuántas palabras tiene el lenguaje 1? "))
    for i in range(num_words_l1):
        word = input(f"Ingrese la palabra {i+1} del lenguaje 1: ")
        l1.append(word)

    l2 = []
    num_words_l2 = int(input("¿Cuántas palabras tiene el lenguaje 2? "))
    for i in range(num_words_l2):
        word = input(f"Ingrese la palabra {i+1} del lenguaje 2: ")
        l2.append(word)

    while True:
        print("\nMenú:")
        print("1. Intersección")
        print("2. Diferencia")
        print("3. Concatenación")
        print("4. Prefijos de una palabra")
        print("5. Sufijos de una palabra")
        print("6. Salir del Sistema")

        choice = input("Elige una opción: ")

        if choice == '1':
            print("El resultado de la intersección es:", intersection(l1, l2))
        elif choice == '2':
            print("El resultado de la diferencia es:", difference(l1, l2))
        elif choice == '3':
            print("El resultado de la concatenación es:", concatenation(l1, l2))
        elif choice == '4':
            word = input("Ingresa una palabra para mostrar los prefijos: ")
            print("Los prefijos de la palabra son:", prefixes(word))
        elif choice == '5':
            word = input("Ingresa una palabra para mostrar los sufijos: ")
            print("Los sufijos de la palabra son:", suffixes(word))
        elif choice == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")

if __name__ == "__main__":
    main()