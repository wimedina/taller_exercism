def is_pangram(sentence):
    repite = False
    contador = 0
    oracion = sentence.lower()
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    if sentence == "":
        return False
    else:
        for i in range(0, len(alfabeto)):
            if alfabeto[i] in oracion:
                contador = oracion.count(alfabeto[i]) 
            if contador == 1:
                contador = 0
                repite = True
            elif contador == 0:
                return False  
    return repite
