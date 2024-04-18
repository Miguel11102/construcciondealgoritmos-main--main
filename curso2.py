class curso:

   """----------------------------------------
    #atributos 
    ------------------------------------------"""

   curso__notas = [3, 5, 3, 2, 3.5, 1, 3.5, 4, 3.5, 5, 4.5, 4.2]

   """--------------------------------------------
    #metodos
    --------------------------------------------"""

   def elementos_Totales(self):
     curso_notas=len(self.curso__notas)
     return curso_notas
    
   def promedio_notas(self):
       suma = 0.0
       indice = 0

       while indice <= 12:
          suma= suma+self.__nota[indice]
          indice +=1
          
          return suma/indice

   def calcularCantidadAProbados(self):
       aprobados = 0
       indice = 0

       while indice <12:
          if (self.__notas[indice]>=3.0)and(self._notas[indice]<=5):
             aprobados+=1
             indice+=1

             return aprobados 

   def calcularCantidadAprobados2(self):
      aprobados = 0

      for indice in range(12):
         if (self.__notas[indice]>=3.0)and(self._notas[indice]<=5):
            aprobados+=1
   
      return aprobados
   
   def calcularCantidadAprobados3(self):
      aprobados= 0
      for nota in self.__notas:
         if nota >= 3.0 and nota <= 5.0:
            aprobados+=1
      
      return aprobados
   
   def calcularMayorNota(self):
      maxima=0
      for nota in self.__nota:
         if nota > maxima:
            maxima = nota
      return maxima
   
   def hacerCurva(self):
      indice = 0
      while indice<12:
         if self.nota[indice]<=4.75:
            self.notas[indice]*=1.05
            indice*=1
            return self.notas  
