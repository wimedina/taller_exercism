def score(word):
    puntaje_1 = ["a","e","i","o","u","l","n","r","s","t"]
    puntaje_2 = ["d","g"]
    puntaje_3 = ["b","c","m","p"]
    puntaje_4 = ["f","h","v","w","y"]
    puntaje_5 = ["k"]
    puntaje_8 = ["j","x"]
    puntaje_10 = ["q","z"]
    puntaje_total = 0   
    for i in range(0, len(word)):
        if word[i].lower() in puntaje_1:
            puntaje_total += 1
        elif word[i].lower() in puntaje_2:
            puntaje_total += 2
        elif word[i].lower() in puntaje_3:
            puntaje_total += 3
        elif word[i].lower() in puntaje_4:
            puntaje_total += 4  
        elif word[i].lower() in puntaje_5:
            puntaje_total += 5
        elif word[i].lower() in puntaje_8:
            puntaje_total += 8
        elif word[i].lower() in puntaje_10:
            puntaje_total += 10         
    return puntaje_total
