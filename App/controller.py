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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def loadData(catalog):
    #sortArtists(catalog)
    #sortPieces(catalog)
    loadinfo(catalog)
   
def obrasdelartista(catalog, name):
    return model.obrasdelartista(catalog, name)

def initCatalog():
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos
def loadArtists(catalog):
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    artists_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in artists_file:
        model.addArtist(catalog, artist)
def loadPieces(catalog):
    piecesfile = cf.data_dir + 'Artworks-utf8-small.csv'
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

def loadName(catalog):
    for piece in lt.iterator(catalog['pieces']):
        ID = piece['ConstituentID'].replace("[",'').replace(']','')
        if mp.contains(catalog['artistsID'], ID):
            entry= mp.get(catalog['artistsID'], ID)
            artist= me.getValue(entry)
        Names=artist['DisplayName'].split(",")
        for name in Names:
            if name!='':
                model.addName(catalog, name, piece)

#opcion 2
def loadMedium(catalog):
    for piece in lt.iterator(catalog['pieces']):
        Medium = piece['Medium']
        if Medium != '':
            model.addMedium(catalog, Medium, piece)
def result(catalog, medio, n):
    return model.result(catalog, medio, n)
def callcmp(date1,date2):
    model.cmp(date1,date2)
    return model.cmp(date1,date2)
def callgetsizemedium(catalog, medium):
    return model.getsizemedium(catalog,medium)

def callgetsizemediumlist(catalog):
    return model.getsizemediumlist(catalog)
#opcion3
def callgetsizenation(catalog,nacionalidad):
    return model.getsizenation(catalog,nacionalidad)
    
def loadAll(catalog):
    loadArtists(catalog)
    loadPieces(catalog)
    loadMedium(catalog)
    loadNationality(catalog)
    loadName(catalog)

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
# Funciones de consulta sobre el catálogo
def countpieces(nacionalidad, catalog):
    return model.countpieces(nacionalidad, catalog)
