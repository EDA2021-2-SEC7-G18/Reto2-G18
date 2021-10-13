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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time


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
        print("--- %s seconds ---" % (time.time() - start_time))
    elif int(inputs[0]) == 2:
        medio = input('1Ingrese medio a buscar: ')
        tamanio = controller.gettamanio(catalog, medio)
        numero = int(input('Ingrese el numero de obras a buscar, como maximo ' + str(tamanio) + ': '))
        
        res = controller.getres(catalog, medio, numero)
        print(res)
    elif int(inputs[0])==3:
        nacionalidad = input('Ingrese la nacionalidad para el conteo de obras: ')
        res = controller.countpieces(nacionalidad, catalog)
        print(res)

    else:
        sys.exit(0)
sys.exit(0)
