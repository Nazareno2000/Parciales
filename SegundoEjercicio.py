

class Cola(object):

    def __init__(self):
        self.__elementos = []
    
    def arribo(self, dato):
        self.__elementos.append(dato)
    
    def atencion(self):
        return self.__elementos.pop(0)
    
    def cola_vacia(self):
        return len(self.__elementos) == 0
    
    def en_frente(self):
        return self.__elementos[0]
    
    def mover_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato
    
    def tamanio(self):
        return len(self.__elementos)

class Notificacion(object):

    def __init__(self,hora,app,mensajes):
        self.hora=hora
        self.app=app
        self.mensajes=mensajes
    
    def __str__(self):
        return str(self.hora) +''+self.app+''+self.mensajes
cola=Cola()  
cola_aux=Cola()  
cola_aux2=Cola()
cola_instagram=Cola()

llegada=Notificacion(12,'facebook','bienvenido')   
cola.arribo(llegada)
llegada=Notificacion(10,'twitter','python')   
cola.arribo(llegada)
llegada=Notificacion(9,'instagram','tus fotos')   
cola.arribo(llegada)
llegada=Notificacion(3,'facebook','hola')   
cola.arribo(llegada)

cantidad=cola.tamanio()
j=0
while(j<cantidad):
   
    if cola.en_frente(j).app=='instagram':
        cola_instagram.arribo(cola.en_frente(j))
    j+=1


while(not cola.cola_vacia()):
    x=cola.en_frente()
    if x.app=='facebook':
        cola.atencion()
    else:
        if x.app =='twitter' and x.mensajes=='python':
            cola_aux.arribo(cola.en_frente())
            cola_aux2.arribo(cola.atencion())
       

print('cola sin facebook')
while(not cola_aux2.cola_vacia()):
    print(cola_aux2.atencion())
print('notificaciones de twitter')
print()
while(not cola_aux.cola_vacia()):
       print(cola_aux.atencion())

while(not cola_instagram.cola_vacia()):
    print(cola_instagram.atencion())