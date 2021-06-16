def __criterio(dato, criterio):
    if(criterio is None):
        return dato
    else:
        return dato[criterio]

def quicksort(vector, inicio, fin, criterio):
    primero = inicio
    ultimo = fin -1
    pivote = fin
    while(primero < ultimo):
        while(__criterio(vector[primero], criterio) <= __criterio(vector[pivote], criterio) and primero <= ultimo):
            primero += 1
        while(__criterio(vector[ultimo], criterio) > __criterio(vector[pivote], criterio) and ultimo >= primero):
            ultimo -= 1
        if(primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if(__criterio(vector[pivote], criterio) < __criterio(vector[primero], criterio)):
        vector[primero], vector[pivote] = vector[pivote], vector[primero]

    if(inicio < primero):
        quicksort(vector, inicio, primero -1, criterio)
    if(fin > primero):
        quicksort(vector, primero + 1, fin, criterio)

class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos = []
    
    def __criterio(self, dato, criterio):
        if(criterio == None):
            return dato
        else:
            return dato[criterio]

    def insertar(self, dato, criterio=None): #! tener en cuenta que la insercion es ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(self.__criterio(dato, criterio) < self.__criterio(self.__elementos[0], criterio)):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while(pos < len(self.__elementos) and self.__criterio(dato, criterio)>=self.__criterio(self.__elementos[pos], criterio)):
                pos +=1 
            self.__elementos.insert(pos, dato) 


    def eliminar(self, dato, criterio=None, clave=None, criterio_clave=None):
        pos = self.busqueda(dato, criterio, clave, criterio_clave)
        if(pos != -1):
            return self.__elementos.pop(pos)
        else:
            return None


    def modificar_elemento(self, pos, nuevo_valor, criterio=None):
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor, criterio)

    def busqueda(self, buscado, criterio=None, clave=None, criterio_clave=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) -1
        while(primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if(self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif(self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio -1
            else:
                primero = medio + 1

        if(pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while(self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos-1], criterio)):
                pos -= 1
            
            while(self.__elementos[pos][criterio_clave] != clave and 
                self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos+1], criterio)):
                pos += 1
            
            if(self.__elementos[pos][criterio_clave] != clave):
                pos = -1

        return pos

        # [1, 2, 3, 4, 4, 4, 5, 6,7]
    
    def obtener_elemento(self, pos):
        if(pos >= 0 ):
            return self.__elementos[pos]
        else:
            return None

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)
    
    def barrido_jedi(self):
        for elemento in self.__elementos:
            print(elemento['name'], elemento['species'])
    
    def barrido_green(self):
        for elemento in self.__elementos:
            if('green' in elemento['lightsaber_color']):
                print(elemento['name'])
    
    def barrido_lista_autos(self):
        for elemento in self.__elementos:
            print(elemento)
            print('autos:')
            elemento['autos'].barrido()

    # def barrido(self):
    #     for elemento in self.__elementos:
    #         for valor in elemento.values():
    #             print(valor)
        
    def barrido_eliminando(self, datos_eliminar):

        for elemento in self.__elementos:
            if(elemento in datos_eliminar):
                self.__elementos.remove(elemento)
    
    def ordenar(self, criterio):
        quicksort(self.__elementos, 0, len(self.__elementos)-1, criterio)


lista_super=Lista()
lista_super2=Lista()

letras=['C','S']
saga = [
        {'name':'Wolverine'},
        {'name':'Linterna Verde'},
        {'name':'Dr. Strange'},
        {'name':'Capitana Marvel'},
        {'name':'Scalet Witch'},
        {'name':'Flash'},
        {'name':'Star-Lord'},
     ]
agregados=[ {'name':'Black Widow,','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'garras'},
            {'name':'hulk','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'garras'},
            {'name':'Rocket Racoonn','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'garras'},
            {'name':'loki','aparicion': 1960, 'casa de comic' : 'DC', 'biografia': 'garras'}    
        ]
for superheroes in saga:
    lista_super.insertar(superheroes,'name')
for nuevos in agregados:
    lista_super2.insertar(nuevos,'name')

posPrimerBuscado=lista_super.busqueda('Thor','name')
if posPrimerBuscado==-1:
    print('no esta')

posScarlet=lista_super.busqueda('Scalet Witch','name')
lista_super.obtener_elemento(posScarlet)['name']='Scarlet Witch'



for i in range(lista_super2.tamanio()):
    aux=lista_super2.obtener_elemento(i)
    if (lista_super.busqueda(aux,'name') ==-1):
        lista_super.insertar(aux,'name')


print(lista_super.obtener_elemento(7))


for i in range(lista_super.tamanio()):
    aux=lista_super.obtener_elemento(i)
    if aux['name'][0] in letras:
        print(aux['name'])
    else:
        print('ninguno lo tiene')   

print('Barrido descendente')
for i in range(lista_super.tamanio()-1, -1 ,-1):
    print(lista_super.obtener_elemento(i))

lista_super3=Lista()
# saga2 = [
#         {'name':'Wolverine','aparicion': 1960, 'casa de comic' : 'DC'},
#         {'name':'Linterna Verde','aparicion': 1970, 'casa de comic' : 'MARVEL'},
#         {'name':'Dr. Strange','aparicion': 1978, 'casa de comic' : 'DC'},
#         {'name':'Capitana Marvel','aparicion': 1976, 'casa de comic' : 'DC', },
#         {'name':'Scalet Witch','aparicion': 1998, 'casa de comic' : 'MARVEL',},
#         {'name':'Flash','aparicion': 1999, 'casa de comic' : 'MARVEL' },
#         {'name':'Star-Lord','aparicion': 1991, 'casa de comic' : 'MARVEL'},
#         {'name':'Black Widow,','aparicion': 1960, 'casa de comic' : 'DC'},
#         {'name':'hulk','aparicion': 1960, 'casa de comic' : 'DC'},
#         {'name':'Rocket Racoonn','aparicion': 1960, 'casa de comic' : 'DC'},
#         {'name':'loki','aparicion': 1960, 'casa de comic' : 'DC'}    
# ]
# for personajes2 in saga2:
#     lista_super3.insertar(personajes2,'name')
# lista_super3.barrido()
# print()
# lista_super3.ordenar('aparicion')
# lista_super3.barrido()