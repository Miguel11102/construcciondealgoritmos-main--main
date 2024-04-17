class curso:

    """----------------------------------------
    #atributos 
    ------------------------------------------"""

    curso_notas = [3, 5, 3, 2, 3.5, 1, 3.5, 4, 3.5, 5, 4.5, 4.2]

    """--------------------------------------------
    #metodos
    --------------------------------------------"""

    def elementos_Totales(self):
     curso_notas=len(self.curso_notas)
     return curso_notas
    
    def promedio_notas(self):
       suma = 0.0
       indice = 0
       while indice <= 12:
          suma= suma+self.__nota[indice]
          indice +=1
          return suma/indice
       
