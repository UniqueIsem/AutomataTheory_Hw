def generate_kleene_closure(words, level):
    if level == 0:
        return [""]
    result = []
    for w in generate_kleene_closure(words, level - 1):
        for word in words:
            result.append(w + word)
    return result


def main():
    while True:
        num_words = int(input("¿Cuántas palabras contiene el lenguaje? "))
        words = []
        for i in range(num_words):
            word = input(f"Ingresa la palabra {i + 1} del lenguaje: ")
            words.append(word)
        kleene_level = int(input("¿Qué nivel de cerradura de Kleene deseas conocer? "))
        result_words = set()
        result_words.update(generate_kleene_closure(words, kleene_level))

        print("El conjunto de palabras que corresponde al nivel", kleene_level, "de cerradura son:")
        for w in sorted(result_words):
            print(w)
        print("Cantidad de palabras:", len(result_words))

        exit_choice = input("¿Deseas continuar? (y|n):")
        if exit_choice.lower() == 'n' or exit_choice == 'N':
            print("Hasta pronto...")
            break
        elif exit_choice.lower() == 'y' or exit_choice == 'Y':
            continue
        else:
            print("Ingrese un valor valido (Y/N)")

if __name__ == "__main__":
    main()