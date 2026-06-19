libros = {
    "python": 5,
    "java": 3,
    "c++": 4
}

prestamos = 0

while True:
    try:
        print("\n--- BIBLIOTECA ---")
        print("1. Prestar")
        print("2. Devolver")
        print("3. Ver stock")
        print("4. Salir")

        op = int(input("Seleccione: "))

        if op == 1:
            libro = input("Libro: ").lower()

            if libro not in libros:
                print("No existe")
                continue

            if libros[libro] <= 0:
                print("Sin stock")
                continue

            libros[libro] -= 1
            prestamos += 1

            print("Préstamo realizado")

        elif op == 2:
            libro = input("Libro: ").lower()

            if libro not in libros:
                print("No existe")
                continue

            libros[libro] += 1
            print("Devuelto")

        elif op == 3:
            for l in libros:
                print(l, "-", libros[l])

        elif op == 4:
            print("Total préstamos:", prestamos)
            break

    except ValueError:
        print("Error")