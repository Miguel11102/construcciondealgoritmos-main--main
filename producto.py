from enum import Enum
"""----------------------------------------------------
#enumeraciones
----------------------------------------------------"""
class tipo(Enum):
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3
class producto:
    __subsidio = False
    __calidad = "A"
    """---------------------------------------------------------------
    # constantes
    ------------------------------------------------------------------"""
    
    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMECADO = 0.04
    __IVA_FARMACIA = 0.12

    PRECIO_MAXIMO = 500000

    """----------------------------------------------------------------
    # Atributos
    -------------------------------------------------------------------"""
    __nombre = None
    __tipo = Enum("tipo",["PAPELERIA", "SUPERMERCADO", "FARMACIA"])
    __valorUnitario = 0.0
    __cantidadBodegas = 0
    __cantidadMinima = 0
    __cantidadUnidadesVendidas = 0

    """-------------------------------------------------------------------
    # Metodos
    --------------------------------------------------------------------"""

    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodegas(self):
        return self.__cantidadBodegas
    
    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
