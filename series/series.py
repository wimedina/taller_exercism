def slices(series, length):
    str_series = []
    if len(series) < length:
        raise ValueError("El tamaño de la cadena debe ser mayor que el tamaño de la subcadena")
    elif length < 0:
        raise ValueError("La longitud de la subcadena no debe ser un número negativo")
    elif length == 0:
        raise ValueError("La longitud de la subcadena no debe ser cero")
    elif series == "":
        raise ValueError("La cadena no debe estar vacía")
    else:
        for i in range(0, len(series)):
            str_series += [(series[i:length+(i*1)])]
            if len(str_series[i]) < length:
                str_series.pop()
                break
    return str_series
