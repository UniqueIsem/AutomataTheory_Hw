def ejemplo_1
    print "Ingrese una cadena de texto: "
    cadena = gets.chomp
    if cadena =~ /1[^2]/
        puts "Cadena VALIDA\n\n"
    else
        puts "NO VALIDO\n\n"
    end
end

def ejemplo_2
    print "Ingrese una cadena de texto: "
    cadena = gets.chomp
    if cadena !~ /\d$/
        puts "Cadena VALIDA\n\n"
    else
        puts "Termina con un dígito (NO VALIDO)\n\n"
    end
end

def mostrar_menu
    puts "MENU"
    puts "1. Ejemplo 1: Comprobar si el String cadena contiene un '1' que no está seguido por un '2'"
    puts "2. Ejemplo 2: Comprobar si el String cadena no acaba con un dígito"
    puts "3. Salir"
end

continuar = true
while continuar
    mostrar_menu
    print "Elija una opción: "
    opcion = gets.chomp
    case opcion
    when '1'
        ejemplo_1
    when '2'
        ejemplo_2
    when '3'
        puts "Saliendo del programa..."
        continuar = false
    else
        puts "Opción inválida, por favor elija una opción del menú\n\n"
    end
end