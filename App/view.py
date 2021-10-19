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
from DISClib.ADT import map as mp
from datetime import datetime
from prettytable import PrettyTable
from DISClib.DataStructures import mapentry as me


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
        print(lt.size(catalog['artists']))
        print("--- %s seconds ---" % (time.time() - start_time))
    elif int(inputs[0]) == 2:
        startdate=str(input('Ingrese la fecha inicial '))
        startdate=datetime.strptime(startdate,'%Y-%m-%d')
        enddate=str(input('Ingrese la fecha final '))
        enddate=datetime.strptime(enddate,'%Y-%m-%d')
        start_time=time.time()
        sortcmp=controller.callbegindatesortcmp
        cmpfunction=controller.callartistrangecmp
        rangemap, Artistcount=controller.callartistrangelist(catalog,cmpfunction,startdate,enddate)
        if rangemap==None:
            print('Artists not found in range')
            break
        keylist=controller.sortlistquick(mp.keySet(rangemap),sortcmp)
        maintable=PrettyTable()
        maintable.field_names = ['DisplayName','BeginDate','EndDate','Nationality','Gender']
        maintable.align='l'
        maintable._max_width= {'DisplayName':30,'BeginDate':10,'EndDate':10,'Nationality':15,'Gender':10}
        first= lt.firstElement(keylist)
        entry1=mp.get(rangemap, str(first))
        value1=me.getValue(entry1)
        sizefirst=lt.size(value1)
        for i in lt.iterator(value1):
            maintable.add_row([str(i['DisplayName']), str(i['BeginDate']), str(i['EndDate']), str(i['Nationality']), str(i['Gender'])])
        last=lt.lastElement(keylist)
        entry2=mp.get(rangemap, str(last))
        value2=me.getValue(entry2)
        sizelast=lt.size(value2)
        for i in lt.iterator(value2):
            maintable.add_row([str(i['DisplayName']), str(i['BeginDate']), str(i['EndDate']), str(i['Nationality']), str(i['Gender'])])
        print('\nThere are '+ str(Artistcount) + ' artists born between ' + str(startdate) + ' and ' + str(enddate))
        print('The first and last 3 artists in range are...\n')
        print(maintable.get_string(start=0, end=3))
        print(maintable.get_string(start=(sizefirst+sizelast)-3, end=sizefirst+sizelast))
        print("--- %s seconds ---" % (time.time() - start_time))
    elif int(inputs[0])==3:
        startdate=str(input('Ingrese la fecha inicial '))
        startdate=datetime.strptime(startdate,'%Y-%m-%d')
        enddate=str(input('Ingrese la fecha final '))
        endyear=datetime.strptime(enddate,'%Y-%m-%d').year
        enddate=datetime.strptime(enddate,'%Y-%m-%d')
        start_time=time.time()
        cmp=controller.callpiecerangecmp
        rangekeys,piececount,Artistcount, purchases=controller.callkeysinrange(catalog, cmp, startdate, enddate)
        if lt.size(rangekeys)==0:
            print('Artworks not found in range')
            break
        sortkeyscmp= controller.callkeysortcmp
        sortedkeys=controller.sortlistquick(rangekeys,sortkeyscmp)
        maintable=PrettyTable()
        maintable.field_names = ['Artists','Title','DateAcquired','Medium','Dimensions']
        maintable.align='l'
        maintable._max_width= {'Artists':12,'Title':50,'DateAcquired':10,'Medium':20,'Dimensions':50}
        totalsize=0
        counter =0
        for i in lt.iterator(sortedkeys):
            entry=mp.get(catalog['DateAcquired'], i)
            value=me.getValue(entry)
            totalsize+=lt.size(value)
            for h in lt.iterator(value):
                ID= str(h['ConstituentID']).replace('[','').replace(']','').replace(' ','')
                ID=ID.split(',')
                Name=''
                for element in ID:
                    entry=mp.get(catalog['artistsID'], element)
                    artist=me.getValue(entry)
                    Name+=str(artist['DisplayName'])
                maintable.add_row([str(Name), str(h['Title']), str(h['DateAcquired']), str(h['Medium']), str(h['Dimensions'])])
            counter+=1
            if counter >=3:
                break
        finalkeys= lt.subList(sortedkeys, lt.size(sortedkeys)-2, 3 )
        counter=0
        for m in lt.iterator(finalkeys):
            entry=mp.get(catalog['DateAcquired'], m)
            value=me.getValue(entry)
            totalsize+=lt.size(value)
            for h in lt.iterator(value):
                ID= str(h['ConstituentID']).replace('[','').replace(']','').replace(' ','')
                ID=ID.split(',')
                for element in ID:
                    entry=mp.get(catalog['artistsID'], element)
                    artist=me.getValue(entry)
                    Name=artist['DisplayName']
                    maintable.add_row([str(Name), str(h['Title']), str(h['DateAcquired']), str(h['Medium']), str(h['Dimensions'])])
            counter+=1
            if counter >=4:
                break
        print('\n The MOMA acquired '+ str(piececount) +' unique pieces between '+ str(startdate) +' and '+ str(enddate)+'\n'+'With '+ str(Artistcount)+' different artists and purchased '+ str(purchases) + ' of them \n')
        print('the first and last 3 artworks in the range are: \n')
        print(maintable.get_string(start=0, end=3))
        print(maintable.get_string(start=(totalsize)-3, end=(totalsize)))
        print("--- %s seconds ---" % (time.time() - start_time))

    elif int(inputs[0])==5:
        nacionalidad = input('Ingrese la nacionalidad para el conteo de obras: ')
        start_time=time.time()
        size=controller.callgetsizenation(catalog, nacionalidad)
        print(size)
        print("--- %s seconds ---" % (time.time() - start_time))

    else:
        sys.exit(0)
sys.exit(0)
