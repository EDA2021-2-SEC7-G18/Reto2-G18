﻿"""
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
 """

from datetime import date
import config as cf
import model
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import quicksort as qck


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos
def loadArtists(catalog):
    artistsfile = cf.data_dir + 'Artists-utf8-large.csv'
    artists_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in artists_file:
        model.addArtist(catalog, artist)
def loadPieces(catalog):
    piecesfile = cf.data_dir + 'Artworks-utf8-large.csv'
    piece_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    for piece in piece_file:
        model.addPiece(catalog,piece)
def loadNationality(catalog):
    for piece in lt.iterator(catalog['pieces']):
        ID = piece['ConstituentID'].replace("[",'').replace(']','')
        if mp.contains(catalog['artistsID'], ID):
            entry= mp.get(catalog['artistsID'], ID)
            artist= me.getValue(entry)
        Nationalities=artist['Nationality'].split(",")
        for nationality in Nationalities:
            if nationality!='':
                model.addNationality(catalog, nationality, piece)
def loadBeginDate(catalog):
    for artist in lt.iterator(catalog['artists']):
        begindate=artist['BeginDate']
        if begindate != '0':
            model.addBeginDate(catalog, begindate, artist)
def loadDateAcquired(catalog):
    for piece in lt.iterator(catalog['pieces']):
            DateAcquired=piece['DateAcquired']
            if DateAcquired != '':
                model.addDateAcquired(catalog, DateAcquired, piece)

#opcion 2
def callbegindatesortcmp(date1,date2):
    return model.begindatesortcmp(date1,date2)
def callartistrangecmp(year,start,end):
    if year != ('0') and year != (''):
        condition=model.cmpartistrange(year,start,end)
    else:
        condition=False
    return condition
def callartistrangelist(catalog, cmpfunction,startdate,endate):
    return model.artistrangelist(catalog, cmpfunction,startdate,endate)
#opcion3
def callpiecerangecmp(date, start, end):
    if start != ('') and end != (''):
        var= model.piecerangecmp(date,start,end)
    else:
        var=False
    return var
def callkeysinrange(catalog, cmp, start, end):
    return model.keysinrange(catalog,cmp,start,end)
def callkeysortcmp(key1, key2):
    if key1 != ('') and key2 != (''):
        condition= model.keysortcmp(key1,key2)
    else:
        condition=False
    return condition
#opcion5
def callgetsizenation(catalog,nacionalidad):
    return model.getsizenation(catalog,nacionalidad)
    
def loadAll(catalog):
    loadArtists(catalog)
    loadPieces(catalog)
    loadNationality(catalog)
    loadBeginDate(catalog)
    loadDateAcquired(catalog)

def loadinfo(catalog):
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    piecesfile = cf.data_dir + 'Artworks-utf8-small.csv'
    piece_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    artists_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    model.loadinfo(piece_file, artists_file, catalog)  #catalog con dos mapas uno con info de los artistas y otro con las piezas. Adicionalmente se carga el indice medium
    model.loadnationality(catalog)
 
def gettamanio(catalog, medio):
    return model.gettamanio(catalog, medio)
def getres(catalog, medio, numero):
    return model.getres(catalog, medio, numero)

def sortArtists(catalog):
    model.sortArtists(catalog)
    
def sortPieces(catalog):
    model.sortPieces(catalog)
# Funciones de ordenamiento
def oldpieces(catalog, medio):
    model.oldpieces(catalog, medio)
def sortlistquick(catalog,cmpfunction):
    return qck.sort(catalog,cmpfunction)
# Funciones de consulta sobre el catálogo
def countpieces(nacionalidad, catalog):
    return model.countpieces(nacionalidad, catalog)
