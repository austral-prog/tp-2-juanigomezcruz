def change():
    expense = 23.75
    money = 100
    gasto = float(input("Ingresar gasto:\n"))
    dinero = float(input("Dinero recibido\n"))
    vuelto = dinero - gasto
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")
