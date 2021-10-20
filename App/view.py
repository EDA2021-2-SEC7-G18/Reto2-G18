"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

#from App.controller import callgetsizemedium
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time
from DISClib.ADT import map as mp


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Las n obras mas antiguas por medio especifico")
    print("3- Cuantas obras por nacionalidad?")
    print("4- Obras de un artista por medio especifico: ")
    print("5- Costo de transportar obras de un departamento ")
catalog = None


def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    return controller.loadAll(catalog)
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        start_time=time.time()
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print(lt.size(catalog['artists']))
        print("--- %s seconds ---" % (time.time() - start_time))
    elif int(inputs[0]) == 2:
        medio = input('Ingrese medio a buscar: ')
        start_time=time.time()
        size=controller.callgetsizemedium(catalog, medio)
        cmp=controller.callcmp
        n = int(input('Ingrese el numero de obras a buscar, como maximo ' + str(size) + ': '))
        selectedmedium = controller.result(catalog, medio, n)
        print(selectedmedium)
        print("--- %s seconds ---" % (time.time() - start_time))
    elif int(inputs[0])==3:
        nacionalidad = input('Ingrese la nacionalidad para el conteo de obras: ')
        start_time=time.time()
        size=controller.callgetsizenation(catalog, nacionalidad)
        print(size)
        print("--- %s seconds ---" % (time.time() - start_time))
    elif int(inputs[0])==4:
        artista = input("Ingrese el artista " )
        artistpieces = controller.obrasdelartista(catalog, artista)
        totalobras = controller.totalobras(artistpieces)
        #print(artistpieces)
        controller.loadspecificpieces(catalog, artistpieces) #carga catalog['specificpiecesmedium']
        #print(catalog['specificpiecesmedium'])
        mediosespecifico =controller.callgetsizemediumlist(catalog)
        mediostotal = controller.mediostotal(mediosespecifico)
        mediomasutilizado = controller.getfirst(mediosespecifico)
        print('Medios totales: ' + str(mediostotal))
        print('Medio mas utilizado ' + str(mediomasutilizado[0]))
        print('Total de obras: ' + str(totalobras))
        controller.sortspecificpieces(catalog)
        pieceinfo = controller.pieceinfo(catalog, mediomasutilizado[0])
        #print(pieceinfo)
        #print(catalog['specificpiecesmedium'])
        #'''
        print('Obra 1: ' +str(pieceinfo[0])+ '\n')
        print('Obra 2: ' +str(pieceinfo[1])+ '\n')
        print('Obra 3: ' +str(pieceinfo[2])+ '\n')
        print('Antepenultima obra: ' +str(pieceinfo[3])+ '\n')
        print('Penultima obra: ' +str(pieceinfo[4])+ '\n')
        print('ultima obra: ' +str(pieceinfo[5])+ '\n')
        #'''
    
    elif int(inputs[0])==5:
        departamento = input("Ingrese un departamento: ")
        #print(catalog['pieces'])
        controller.loaddepartment(catalog)
        #totalobras = controller.totalobrasdepartment(catalog, departamento)
        res = controller.dimensions(catalog, departamento)
        print(res)
    else:
        sys.exit(0)
sys.exit(0)
