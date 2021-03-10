import unittest 
from motor_tablero import Tablero

class TestTaTeTi(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_casillero_vacio_vacio(self):
        assert self.tablero.es_coordenada_vacia(0,0) == True

    def test_casillero_vacio_ocupado(self):
        self.tablero.jugar_en_coordenada(0,0, "X")

        assert self.tablero.es_coordenada_vacia(0,0) == False

    def test_obtener_coordenada_valor_correcto(self):
        assert self.tablero.obtener_coordenada(1,1) == "-"
    
    def test_obtener_coordenara_valor_incorrecto(self):
        self.tablero.jugar_en_coordenada(1,1, "O")
        
        assert self.tablero.obtener_coordenada(1,1) != "X"
    
    def test_diagonal_principal_iguales(self):
        self.tablero.jugar_en_coordenada(0,0, "X")
        self.tablero.jugar_en_coordenada(1,1, "X")
        self.tablero.jugar_en_coordenada(2,2, "X")

        assert self.tablero.diagonal_principal_con_fichas_iguales() == True
    
    def test_diagonal_principal_distintos(self):
        self.tablero.jugar_en_coordenada(0,0, "X")
        self.tablero.jugar_en_coordenada(1,1, "X")
        self.tablero.jugar_en_coordenada(2,2, "O")

        assert self.tablero.diagonal_principal_con_fichas_iguales() == False       

    def test_diagonal_inversa_iguales(self):
        self.tablero.jugar_en_coordenada(0,2, "O")
        self.tablero.jugar_en_coordenada(1,1, "O")
        self.tablero.jugar_en_coordenada(2,0, "O")

        assert self.tablero.diagonal_inversa_con_fichas_iguales() == True

    def test_diagonal_inversa_distintos(self):
        self.tablero.jugar_en_coordenada(0,2, "O")
        self.tablero.jugar_en_coordenada(1,1, "O")
        self.tablero.jugar_en_coordenada(2,0, "X")

        assert self.tablero.diagonal_inversa_con_fichas_iguales() == False

    def test_fila_iguales_correcto(self):
        self.tablero.jugar_en_coordenada(0,0, "X")
        self.tablero.jugar_en_coordenada(0,1, "X")
        self.tablero.jugar_en_coordenada(0,2, "X")

        assert self.tablero.fila_con_fichas_iguales(0) == True

    def test_fila_iguales_incorrecto(self):
        self.tablero.jugar_en_coordenada(1,0, "X")
        self.tablero.jugar_en_coordenada(1,1, "X")
        self.tablero.jugar_en_coordenada(1,2, "O")

        assert self.tablero.fila_con_fichas_iguales(1) == False

    def test_columna_iguales_correcto(self):
        self.tablero.jugar_en_coordenada(0,2, "O")
        self.tablero.jugar_en_coordenada(1,2, "O")
        self.tablero.jugar_en_coordenada(2,2, "O")

        assert self.tablero.columna_con_fichas_iguales(2) == True

    def test_columna_iguales_incorrecto(self):
        self.tablero.jugar_en_coordenada(0,0, "O")
        self.tablero.jugar_en_coordenada(1,0, "X")
        self.tablero.jugar_en_coordenada(2,0, "O")

        assert self.tablero.columna_con_fichas_iguales(0) == False
