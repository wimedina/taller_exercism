def is_isogram(string):
    repite = False
    contador_igual = 0
    if string == "":
        repite = True
    else:
        for i in range(0, len(string)):
            if "-" in string[i] or " " in string[i]:
                continue     
            for j in range(0, len(string)):
                if string[i].lower() == string[j].lower():
                    contador_igual += 1       
            if contador_igual == 1:
                contador_igual = 0
                repite = True            
            else:
                repite = False              
    return repite
