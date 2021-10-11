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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def loadData(catalog):
    #sortArtists(catalog)
    #sortPieces(catalog)
    loadinfo(catalog)
   


def initCatalog():
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos

def loadinfo(catalog):
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    piecesfile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    piece_file = csv.DictReader(open(piecesfile, encoding='utf-8'))
    artists_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    model.loadinfo(piece_file, artists_file, catalog)  #catalog con dos mapas uno con info de los artistas y otro con las piezas. Adicionalmente se carga el indice medium
 
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
