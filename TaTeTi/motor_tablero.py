

class Tablero:
    VACIA = "-"
    matriz = None

    def __init__(self):
        self.matriz = [
            [self.VACIA, self.VACIA, self.VACIA],
            [self.VACIA, self.VACIA, self.VACIA],
            [self.VACIA, self.VACIA, self.VACIA]
        ]
    
    def jugar_en_coordenada(self, fila, columna, ficha):
        self.matriz[fila][columna] = ficha

    def obtener_coordenada(self, fila, columna):
        return self.matriz[fila][columna]

    def es_coordenada_vacia(self, fila, columna):
        return self.obtener_coordenada(fila, columna) == self.VACIA

    def fila_con_fichas_iguales(self, fila):
        return(self.es_coordenada_vacia(fila,0) != True and self.obtener_coordenada(fila,0) == self.obtener_coordenada(fila,1) and 
        self.obtener_coordenada(fila,1) == self.obtener_coordenada(fila,2))
    
    def columna_con_fichas_iguales(self, columna):
        return(self.es_coordenada_vacia(0, columna) != True and self.obtener_coordenada(0, columna) == self.obtener_coordenada(1, columna) and 
        self.obtener_coordenada(1, columna) == self.obtener_coordenada(2, columna))

    def diagonal_principal_con_fichas_iguales(self):
        return(self.es_coordenada_vacia(0,0) != True and self.obtener_coordenada(0,0) == self.obtener_coordenada(1,1) and 
        self.obtener_coordenada(1,1) == self.obtener_coordenada(2,2))

    def diagonal_inversa_con_fichas_iguales(self):
        return(not(self.es_coordenada_vacia(0,2)) and self.obtener_coordenada(0,2) == self.obtener_coordenada(1,1) and 
        self.obtener_coordenada(1,1) == self.obtener_coordenada(2,0))

    # hacer conversion a STR
    
    #def __str__(self):
     #   plantilla = {}




    # # NO SIRVE. Busca en casi todos los casillero y desencadena en resultados
    # no deseados
    # def iteracion_fila_columna(self, fila = 0, columna = 0):
    #    esta_ocupada = True
    #    for i in range(fila, i <= 2):
    #        for j in range(columna, j <= 2):
    #            if(self.es_coordenada_vacia(i,j)):
    #                esta_ocupada = False
    #                break
    #    return esta_ocupada 


        

    