"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'artists': None,
                'pieces': None,
                'medium': None
               }
    
    
    catalog['artists'] = mp.newMap(maptype='PROBING', loadfactor=1)
    catalog['pieces'] = mp.newMap(maptype='PROBING', loadfactor=1)
    catalog['medium'] = mp.newMap(maptype='PROBING', loadfactor=1)
    #mp.put(catalog['medium'], 'llaveee', 'valorr')
    return catalog
def newmap():
    return mp.newMap()

def put():
    return mp.put()


# Funciones para agregar informacion al catalogo

def loadinfo(piece_file, artists_file, catalog):
  
    for artisttemp in artists_file:   #Crea map con constituentID y la info de los artistas
        constituentID = artisttemp['ConstituentID']
        #artisttemp.pop('ConstituentID')
        mp.put(catalog['artists'],constituentID, artisttemp)
    
    lista = lt.newList('ARRAY_LIST')
    diccionariotemp = {}
    for piece in piece_file:
        IDSU = reemplazar(piece)
        piece['ConstituentID'] = modvarios(IDSU) #divide en lista los ID
        pieceID =  piece['ObjectID']
        piece.pop('ObjectID')
        mp.put(catalog['pieces'],pieceID, piece )
        

        elemento = [piece['Medium'], piece['Title'], piece['Date']]
        lt.addLast(lista, elemento)
        #for medioit in lt.iterator(catalog['medium']):
    
    merge.sort(lista, sortoldpieces)
    
    for elemento in lt.iterator(lista):
        
        if diccionariotemp.get(elemento[0]) != None:
            diccionariotemp[elemento[0]].append([elemento[1], elemento[2]])
        else:
            diccionariotemp[elemento[0]] = [[elemento[1], elemento[2]]]
        #return elemento
    for medio in diccionariotemp:
        mp.put(catalog['medium'],medio,diccionariotemp[medio])  #mapa con array dentro con estructura: {medio:[titulo, anio],medio:[titulo, anio] }
    
def gettamanio(catalog, medio):
    pareja = mp.get(catalog['medium'], medio)
    return len(me.getValue(pareja))
 

def getres(catalog, medio, numero):
    pareja = mp.get(catalog['medium'], medio)
    return me.getValue(pareja)[numero][0]

        
def modvarios(IDSU):
    ID = IDSU
    if ", " in IDSU:
        ID = IDSU.split(", ")
    return ID

def reemplazar(uno):

    uno = str(uno["ConstituentID"]).replace("[",'')
    uno =uno.replace(']', '')
    return uno

def sortArtists(catalog):
    sa.sort(catalog['artists'], comparebirthday)


def sortPieces(catalog):
    merge.sort(catalog['pieces'], comparedate)
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def comparebirthday(firstArtist, secondArtist):
    return (int(firstArtist['BeginDate']) < int(secondArtist['BeginDate']))


# Funciones de ordenamiento
def sortoldpieces(pieceone, piecetwo):
    return pieceone[2]<piecetwo[2]
def fixdatePieces(piecelist):
    
    stringprev = str(piecelist['DateAcquired'])
    if (len(stringprev)==0):
        piecelist['DateAcquired']=-1
        return piecelist
    i = "0123456789"
    o=0
    for n in stringprev[0:4]:
        if n not in i:
            piecelist['DateAcquired']=-1
            return piecelist       
    year = int(stringprev[0:4]) 

    if len(stringprev) >= 6:
        if stringprev[5] in i:
            month = int(stringprev[5])*0.1
            year = year + month 
            
            if len(stringprev) >= 7:
                if stringprev[6] in i:
                    monthd = int(stringprev[6])*0.01
                    year = year + monthd
                    
                    #'''
                    if len(stringprev) >= 9:
                        if stringprev[8] in i:
                            day = int(stringprev[8])*0.001
                            year = year + day
                            
                            if len(stringprev) == 10:
                                if stringprev[9] in i:
                                    dayd = int(stringprev[9])
                                    dayd = dayd*0.0001
                                    year = year + dayd
                                    year = round(year,4)
                                    #return round(year,4)
    #'''
    piecelist['DateAcquired']=float(year)
    return piecelist
