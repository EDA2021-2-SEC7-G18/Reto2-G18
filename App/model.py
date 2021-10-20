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


from sys import call_tracing
from typing import OrderedDict
from App.controller import sortlistquick
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
import DISClib.Algorithms.Sorting.quicksort as qck
from datetime import datetime
import re

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'artists': None,
                'artistsID': None,
                'pieces': None,
                'piecesID': None,
                'medium': None,
                'nationality':None,
                'BeginDate':None,
                'DateAcquired':None,
                'name':None,
                'specificpiecesmedium':None,
                'departments':None

               }
    
    
    catalog['artistsID'] = mp.newMap(maptype='PROBING', loadfactor=0.5)
    catalog['artists'] =lt.newList('ARRAY_LIST', cmpfunction=None)
    catalog['piecesID'] = mp.newMap(maptype='PROBING', loadfactor=0.5)
    catalog['pieces'] =lt.newList('ARRAY_LIST', cmpfunction=None)
    catalog['medium'] = mp.newMap(maptype='CHAINING', loadfactor=2.00)
    catalog['nationality'] = mp.newMap(maptype='CHAINING', loadfactor=4.00)
    catalog['BeginDate'] = mp.newMap(maptype='PROBING', loadfactor=0.5)
    catalog['DateAcquired'] = mp.newMap(maptype='PROBING', loadfactor=0.5)
    catalog['name'] = mp.newMap(maptype='CHAINING', loadfactor=2.00)
    catalog['specificpiecesmedium'] = mp.newMap(maptype='CHAINING', loadfactor=2.00)
    catalog['departments'] = mp.newMap(maptype='CHAINING', loadfactor=2.0)

    
    return catalog
def newmap():
    return mp.newMap()

def put():
    return mp.put()


# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    lt.addLast(catalog['artists'], artist)
    mp.put(catalog['artistsID'], artist['ConstituentID'], artist)
def addPiece(catalog, piece):
    lt.addLast(catalog['pieces'], piece)
    mp.put(catalog['piecesID'], piece['ConstituentID'],piece)

def addNationality(catalog, Nationality, piece):
    nationalities= catalog['nationality']
    exisnationality = mp.contains(nationalities, Nationality)
    if exisnationality:
        entry = mp.get(nationalities, Nationality)
        nation = me.getValue(entry)
    else:
        nation = lt.newList('ARRAY_LIST',cmpfunction=None)
        mp.put(nationalities, Nationality, nation)
    lt.addLast(nation, piece)
def addBeginDate(catalog, date, Artist):
    dates= catalog['BeginDate']
    existdate = mp.contains(dates, date)
    if existdate:
        entry = mp.get(dates, date)
        value = me.getValue(entry)
    else:
        value = lt.newList('ARRAY_LIST',cmpfunction=None)
        mp.put(dates, date, value)
    lt.addLast(value, Artist)
def addDateAcquired(catalog, date, piece):
    dates= catalog['DateAcquired']
    existdate = mp.contains(dates, date)
    if existdate:
        entry = mp.get(dates, date)
        value = me.getValue(entry)
    else:
        value = lt.newList('ARRAY_LIST',cmpfunction=None)
        mp.put(dates, date, value)
    lt.addLast(value, piece)
def adddepartment(catalog, piece, department):
    departments = catalog['departments']
    existdepartment = mp.contains(departments, department)
    if existdepartment:
        entry = mp.get(departments, department)
        lista = me.getValue(entry)
    else:
        lista = lt.newList('ARRAY_LIST', cmpfunction=None)
        mp.put(departments, department, lista)
    lt.addLast(lista, piece)

#opcion2
def begindatesortcmp(Year1,Year2):
    if str(Year1) !=str('0') and str(Year2) !=str('0'):
        condition= datetime.strptime(Year1,'%Y') < datetime.strptime(Year2,'%Y')
    else:
        condition=False
    return condition
def cmpartistrange(year,start,end):
    return datetime.strptime(str(year),'%Y') >= start and datetime.strptime(str(year),'%Y')<=end
def artistrangelist(catalog, cmp, start, end):
    newmap=mp.newMap(maptype='PROBING', loadfactor=0.5)
    Artistcount=0
    for item in lt.iterator(mp.keySet(catalog['BeginDate'])):
        entry=mp.get(catalog['BeginDate'], item)
        group = me.getValue(entry)
        size= lt.size(group)
        if item != None:
            if cmp(item,start,end):
                Artistcount+=size
                mp.put(newmap,item, group)
    return newmap,Artistcount
  
#opcion3
def piecerangecmp(date, start, end):
    return datetime.strptime(date,'%Y-%m-%d')>=start and datetime.strptime(date,'%Y-%m-%d')<=end
def keysinrange(catalog, cmp, start, end):
    newlist= lt.newList('ARRAY_LIST',cmpfunction=None)
    keys= mp.keySet(catalog['DateAcquired'])
    Artistcount= 0
    purchases = 0
    piececount= 0
    IDlist=[]
    for item in lt.iterator(keys):
        entry=mp.get(catalog['DateAcquired'], str(item))
        group = me.getValue(entry)
        size= lt.size(group)
        if item != (''):
            if cmp(item, start,end):
                piececount+=size
                lt.addLast(newlist, item)
                for n in lt.iterator(group):
                    if n['CreditLine']== 'Purchase':
                        purchases +=1
                    ID=n['ConstituentID']
                    if ID not in IDlist:
                        Artistcount += 1
                        IDlist.append(ID)
    return newlist, piececount, Artistcount, purchases 
def dateacquiredsortcmp(Year1,Year2):
    if str(Year1) !=str('') and str(Year2) !=str(''):
        condition= datetime.strptime(Year1,'%Y-%m-%d') < datetime.strptime(Year2,'%Y-%m-%d')
    else:
        condition=False
    return condition
def keysortcmp(key1,key2):
    return datetime.strptime(key1,'%Y-%m-%d') < datetime.strptime(key2,'%Y-%m-%d')
#opcion5
def getsizenation(catalog,nacionalidad):
    entry= mp.get(catalog['nationality'], nacionalidad)
    getval=me.getValue(entry)
    return lt.size(getval)
def setup(catalog):
    keys=mp.keySet(catalog['nationality'])
    newlist=lt.newList('ARRAY_LIST', cmpfunction=None)
    for item in lt.iterator(keys):
        dict = OrderedDict()
        entry=mp.get(catalog['nationality'], item)
        value=me.getValue(entry)
        size=lt.size(value)
        if item != (''):
            dict['key']=item
            dict['value']= size
            lt.addLast(newlist, dict)
    return newlist
def keysort(key1,key2):
    return int(key1['value'])>int(key2['value'])
def newmapnations(lst):
    nmap=mp.newMap(maptype='PROBING', loadfactor=0.5)
    for item in lt.iterator(lst):
        key=item['key']
        size=item['value']
        mp.put(nmap, key, size)
    return nmap
#opcion6
def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False
def dateacquiredcmp(piece1,piece2):
    return int(piece1['Date'])< int(piece2['Date'])
def costcmp(price1,price2):
    return price1['TransCost USD']>price2['TransCost USD']
def cost(catalog, department):
    newlist=lt.newList('ARRAY_LIST', cmpfunction=None)
    entry=mp.get(catalog['departments'], department)
    value=me.getValue(entry)
    sizedepartment= lt.size(value)
    sumatoria=0
    peso=0
    for piece in lt.iterator(value):
        costlist=[]
        if piece['Dimensions'] != '':
            dimension= piece['Dimensions'].replace('cm','').replace('x',',')
            result=re.findall(r'\(.*?\)', dimension)
            if len(result) != 0:
                list=result[0].replace('(','').replace(')','').split(',')
                totalsize=1
                for i in list:
                    if check_float(i):
                        totalsize*=float(i)
                cost=(totalsize/(pow(10,2*len(list))))*72.00
                costlist.append(cost)
            if piece['Weight (kg)']!= '':
                cost=float(piece['Weight (kg)'])*72.00
                costlist.append(cost)
                peso+=float(piece['Weight (kg)'])
            elif piece['Weight (kg)']== ('') and len(result) == 0:
                cost=48.00
                costlist.append(cost)
            finalcost=round(max(costlist),3)
            sumatoria+=finalcost
            piece['TransCost USD']=finalcost
            lt.addLast(newlist, piece)
    return newlist,sumatoria, sizedepartment, peso

#----------------------------   
def loadinfo(piece_file, artists_file, catalog):
  
    for artisttemp in artists_file:   #Crea map con constituentID y la info de los artistas
        
        #artisttemp.pop('ConstituentID')
        mp.put(catalog['artists'],artisttemp['ConstituentID'], artisttemp)
    
    lista = lt.newList('ARRAY_LIST')
    diccionariotemp = {}
    for piece in piece_file:           #INDICE PIECES
        IDSU = reemplazar(piece)
        piece['ConstituentID'] = modvarios(IDSU) #divide en lista los ID
        mp.put(catalog['pieces'],piece['ObjectID'], piece )  #Crea map indice de pieces
        

        elemento = [piece['Medium'], piece['Title'], piece['Date']] #PARTE DE CARGA DE  indice MEDIUM
        lt.addLast(lista, elemento)
   
    for elemento in lt.iterator(lista):  
        
        if diccionariotemp.get(elemento[0]) != None:
            diccionariotemp[elemento[0]].append([elemento[1], elemento[2]])
        else:
            diccionariotemp[elemento[0]] = [[elemento[1], elemento[2]]]
        #return elemento
    for medio in diccionariotemp:
        mp.put(catalog['medium'],medio,diccionariotemp[medio])  #mapa con array dentro con estructura: {medio:[titulo, anio],medio:[titulo, anio] }
    

def loadnationality(catalog):
    piecesID = mp.keySet(catalog['pieces'])
    diccionario = {}
    for pieceID in lt.iterator(piecesID):
        
        piecepair = mp.get(catalog['pieces'], pieceID)
        piecevalue = me.getValue(piecepair) #valor de catalog['pieces] iterado
        
        lista = []
        
        
        if type(piecevalue['ConstituentID']) != list: 
            infoartistpair = mp.get(catalog['artists'], piecevalue['ConstituentID'])
            nationality = me.getValue(infoartistpair)['Nationality']
            lista.append(nationality)

        else:
            
            for ID in piecevalue['ConstituentID']:
                infoartistpair = mp.get(catalog['artists'], ID)
                nationality = me.getValue(infoartistpair)['Nationality']
                if nationality not in lista:
                    lista.append(nationality)
        
        for nacionalidad in lista:
            if diccionario.get(nacionalidad) != None:
                diccionario[nacionalidad].append(piecevalue)
            else: 
                diccionario[nacionalidad]=[piecevalue]

    #catalog['nationality'] = diccionario.keys()
    for llave in diccionario:

        mp.put(catalog['nationality'], llave, diccionario[llave])
    
    

def gettamanio(catalog, medio):
    pareja = mp.get(catalog['medium'], medio)
    return len(me.getValue(pareja))
 

def getres(catalog, medio, numero):
    pareja = mp.get(catalog['medium'], medio)
    valor = me.getValue(pareja)
    lista = lt.newList('ARRAY_LIST')
    for a in valor:
        lt.addLast(lista, a)
    
    merge.sort(lista, sortoldpieces)
    res= []
    i=0
    for b in lt.iterator(lista):
        if i<numero:
            res.append(b[0])
        i+=1
    return res 

        
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


# Funciones para creacion de datos

# Funciones de consulta
def countpieces(nacionalidad, catalog):
    obraspair = mp.get(catalog['nationality'], nacionalidad)
    resprev = me.getValue(obraspair)
    res = len(resprev)
    #return catalog['nationality']
    return res
# Funciones utilizadas para comparar elementos dentro de una lista
def comparebirthday(firstArtist, secondArtist):
    return (int(firstArtist['BeginDate']) < int(secondArtist['BeginDate']))


# Funciones de ordenamiento
def sortoldpieces(pieceone, piecetwo):
    return pieceone[1]<piecetwo[1]
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
