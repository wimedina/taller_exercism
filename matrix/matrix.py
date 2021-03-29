class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        posicion = []
        a = []
        lista = self.matrix_string.split('\n')
        for i in range(0, len(lista)):
            aux = []
            aux_cadena = []
            aux = lista[i]
            aux_cadena = aux.split(' ')
            c = []
            for j in range(0, len(aux_cadena)):
                c = c + [int(aux_cadena[j])]
            a.append(c)
        if index == 0:
            return -1
        else:
            posicion = a[index - 1]
            return posicion

    def column(self, index):
        a = []
        columna = []
        lista = self.matrix_string.split('\n')
        for i in range(0, len(lista)):
            aux = []
            aux_cadena = []
            aux = lista[i]
            aux_cadena = aux.split(' ')
            c = []
            for j in range(0, len(aux_cadena)):
                c = c + [int(aux_cadena[j])]
            a.append(c)
        for m in range(0, len(a)):
            columna += [int(a[m][index - 1])]
        return columna
