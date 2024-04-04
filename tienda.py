from producto import producto
class tienda:

    """-------------------------------------------------------
    #Atributos
    --------------------------------------------------------"""

    #__producto1 = None
    #__producto2 = None
    #__producto3 = None
    #__producto4 = None

    """--------------------------------------------------------------
    #metodos
    --------------------------------------------------------------"""
    def __init__(self):
        self.__producto1 = producto("Papeleria", "lapiz", 550.0, 18, 5)
        self.dineroEnCaja = 0

    def __init__(self):
        self.__producto2 = producto("Supermercado", "Cafe", 5600.0,30, 9)
        self.dineroEnCaja = 0

    def __init__(self):
        self.__producto3 = producto("Papeleria", "Borrador", 300.0, 15 ,5)
        self.dineroEnCaja = 0

    def __init__(self):
        self.__producto4 = producto("Drogueria", "desinfectante", 3200.0, 12, 11)
        self.dineroEnCaja = 0


    def getProducto1(self):
        return self.__producto1
    
    def getProducto2(self):
        return self.__producto2
    
    def getProducto2(self):
        return self.__producto3
    
    def getProducto2(self):
        return self.__producto4
