def distance(strand_a, strand_b):
    cont_diferencial = 0
    if len(strand_a) == len(strand_b):
        for i in range(0, len(strand_a)):
            if strand_a[i] != strand_b[i]:
                cont_diferencial += 1
    else:
        raise ValueError("Las cadenas deben tener el mismo tamaño")
    return cont_diferencial
