class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Numero de llamadas realizadas
    numeroLlamadas=""
    # Numero de minutos consumidos
    numeroMinutos=""
    # Costo total de las llamadas
    costoLlamadas=""
    #Estrato de la linea
    estrato=""
    #descuento aplicable a las llamadas (valor entre 0.0 y 25.5)
    descuento= 0.0
    #cantidad de dinero disponible para gastar (prepago)
    prepago= 0.0
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        self.numeroLlamadas = 0
        self.numerominutos = 0
        self.costoLlamadas =0
        # TODO Parte2 PuntoA: Completar el método según la documentación dada.

    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        return self.costoLlamadas
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        
    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        return self.numeroLlamadas
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        return self.numerominutos
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        self.numeroLlamadas=0
        self.numerominutos=0
        self.costoLlamadas=0
        # TODO Parte2 PuntoE: Completar el método según la documentación dada.

    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.

    def agregarLlamadalocal(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos 
        self.costoLlamadas += pMinutos * 35
   
    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
    
        """
    
    def agregarLlamadaLargaDistancia(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos 
        self.costoLlamadas += pMinutos * 380
        # TODO Parte2 PuntoF: Completar el método según la documentación dada.

    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self, pMinutos):
        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos 
        self.costoLlamadas += pMinutos * 999

    def darDescuento(self):
        return self.descuento
    
    def aplicarDescuento(self):
        return (self.costoLlamadas * self.descuento) / 100
    
    def DarSaldoDisponible(self):
        return self.prepago
    
    def agregarDineroASaldo(self, valor):
        self.prepago += valor
    
    def agregarLlamadalocal (self, pMinutos):
        #incrementa el numero de llamadas
        numeroDeLlamadas = numeroDeLlamadas + 1

        #incrementa el numero de minutos
        numeroMinutos = numeroMinutos + pMinutos 

        #incrementa el costo de las llamadas
        costoLlamadas = costoLlamadas + (pMinutos * 35)
    
    def motivacionCliente(sel, minutosGastados):
        #calcular cuantos bloques de tiempo de 30 minutos se ha gastado el cliente
        bloques = minutosGastados / 30
        #calcular el monto total ganado por el cliente
        montoTotal = bloques * 1000
        return montoTotal
    


