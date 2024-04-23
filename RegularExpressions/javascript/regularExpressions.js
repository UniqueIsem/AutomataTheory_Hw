const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function showMenu() {
    console.log("MENU")
    console.log("1. Validar Email")
    console.log("2. Comprobar tamaño de string")
    console.log("3. Reemplazar letras 'a' y 'c'")
    console.log("4. Salir")
    getMenuOption();
}
function getMenuOption() {
    rl.question('Elija una opcion: ', (opcion) => {
        switch (opcion) {
            case '1':
                // Ejemplo 1: Validar email
                const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                rl.question('Ingresa un email: ', (email) => {
                    const match = emailPattern.test(email);
                    if (match) {
                        console.log("Email VALIDO\n\n");
                    } else {
                        console.log("Email NO VALIDO\n\n")
                    }
                    showMenu();
                })
                break;
            case '2': 
                //Comprobar si el String cadena está formado por un mínimo de 5 letras mayúsculas o minúsculas y un máximo de 10.
                const stringPattern = /^[a-zA-Z]{5,10}$/;
                rl.question('Escribe un string y se validará si tiene un valor minimo de 5 y un maximo de 10: ', (userText) => {
                    const match = stringPattern.test(userText);
                    if (match) {
                        console.log('La cadena CUMPLE con los requisitos\n\n')
                    } else {
                        console.log('La cadena NO CUMPLE con los requisitos\n\n')
                    }
                    showMenu();
                });
                
                break;
            case '3':
                // Ejemplo 2: Reemplazar las letras a y c en una cadena
                const pattern2 = /a?c|c?a/g;
                rl.question('Ingrese un texto y se reemplazaran las letras a y c: ', (text2) => {
                    newText = text2.replace(pattern2, 'X');
                    console.log('Texto modificado:', newText, "\n\n");
                    showMenu();
                })
                break;
            case '4':
                console.log("Saliendo del programa");
                break;
            default:
                console.log("Elija una opcion valida\n\n");
                showMenu();
                break;
        }
    });
}

showMenu();
getMenuOption();