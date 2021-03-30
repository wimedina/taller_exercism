def convert(number):
    resultado = ""
    for i in range(1, number + 1):
        if i == 3:
            if number % i == 0:
                resultado += "Pling"
        elif i == 5:
            if number % i == 0:
                resultado += "Plang"
        elif i == 7:
            if number % i == 0:
                resultado += "Plong"
    if resultado == "":
        return str(number)
    else:
        return resultado
