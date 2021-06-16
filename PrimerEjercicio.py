vectorSaga=['luck','yoda','mike']

def barrido (vector,pos):
    if vector==[]:
        return 'NO HAY PERSONAJES'
    else:
        if pos<len(vector):
            return  vector[pos]+ str(barrido(vector,pos+1))
print(barrido(vectorSaga,0))
# #QUERIA SABER SI DE LA PRIMERA MANERA TAMBIEN SE PUEDE

def barrido2(vector):
    if len(vector)>0:
        print(vector[0])
        barrido2(vector[1:])

print(barrido2(vectorSaga))

pos=0
def EncontrarYoda(vector,pos):
    if (pos<len(vector)):
        if (vector[pos]=='yoda'):
            return pos
        else:
            return EncontrarYoda(vector,pos+1)
    else:
         return-1    

if pos!=-1:
    print('el objeto fue encontrado en la posicion ' + str(EncontrarYoda(vectorSaga,0)))


