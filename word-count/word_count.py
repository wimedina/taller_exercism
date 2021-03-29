def count_words(sentence):
    import re
    i = 0
    c = []
    d = []
    aux = ""
    arrAux = []
    palabras = {}
    contador = 0
    a = sentence.lower()
    b = re.compile(r'\W+').split(a)
    for i in range(0, len(b)):
        if b[i] != '':
            c.append(b[i])
    for j in range(0, len(c)):
        if c[j] == "don" and c[j + 1] == "t":
            aux = "don't"
            d.append(aux)
        elif c[j] == "can" and c[j + 1] == "t":
            aux = "can't"
            d.append(aux)
        elif '_' in c[j]:
            arrAux = c[j].split('_')
            for m in arrAux:
                d.append(m)
        else:
            if c[j] != 't':
                d.append(c[j])
    for n in range(0, len(d)):
        contador = d.count(d[n])
        palabras[d[n]] = contador
    return(palabras)
