import sqlite3
import json


def getGeoData(nameSimpul):
    #Membaca data dan menembalikan file json dari geodata dengan addrees = namasimpul
    path = "sqlite/"
    conn = sqlite3.connect(path+'DataGeoLoad.sqlite3')
    cur = conn.cursor()
    find = 'SELECT * FROM Locations WHERE address LIKE ?'
    keyFind = (nameSimpul,)
    cur.execute(find,keyFind)
    for row in cur:
        geodata = str(row[1])
        geodata = json.loads(str(geodata))

    return geodata

def getGeoDataAll():
    path = "sqlite/"
    conn = sqlite3.connect(path+'DataGeoLoad.sqlite3')
    cur = conn.cursor()
    find = 'SELECT * FROM Locations'
    listgeodata = list()
    cur.execute(find)
    for row in cur:
        geodata = str(row[1])
        listgeodata.append( json.loads(str(geodata)))

    return listgeodata


def getSimpulAll():
    path = "sqlite/"
    conn = sqlite3.connect(path+'DataGeoLoad.sqlite3')
    cur = conn.cursor()
    find = 'SELECT * FROM Locations'
    listgeodata = list()
    cur.execute(find)
    for row in cur:
        geodata = str(row[0])
        listgeodata.append(str(geodata))

    return listgeodata


def getLit(nameSimpul):
    #mengembalikan Lit dari namasimpul
    DictGeoData = getGeoData(nameSimpul)
    return DictGeoData['lit']


def getLng(nameSimpul):
    #mengembalikan Lng dari namasimpul
    DictGeoData = getGeoData(nameSimpul)
    return DictGeoData['lng']

def getLitLng(nameSimpul):
    return [getLit(nameSimpul),getLng(nameSimpul)]

def getTetangga(nameSimpul):
    #mengembalikan List of tetangga dari namasimpul
    DictGeoData = getGeoData(nameSimpul)
    return DictGeoData['tetangga']

def getMaxLitAll():
    count = 0
    for Text_JSON in getGeoDataAll():
        if count == 0 :
            MAX_Lit = float(Text_JSON['lit'])
            count +=1
        elif MAX_Lit < float(Text_JSON['lit']) :
            MAX_Lit = float(Text_JSON['lit'])
    
    return MAX_Lit

def getMinLitAll():
    count = 0
    for Text_JSON in getGeoDataAll():
        if count == 0 :
            MIN_Lit = float(Text_JSON['lit'])
            count +=1
        elif MIN_Lit > float(Text_JSON['lit']) :
            MIN_Lit = float(Text_JSON['lit'])
    
    return MIN_Lit


def getMaxLngAll():
    count = 0
    for Text_JSON in getGeoDataAll():
        if count == 0 :
            MAX_Lng = float(Text_JSON['lng'])
            count +=1
        elif MAX_Lng < float(Text_JSON['lng']) :
            MAX_Lng = float(Text_JSON['lng'])
    
    return MAX_Lng

def getMinLngAll():
    count = 0
    for Text_JSON in getGeoDataAll():
        if count == 0 :
            MIN_Ling = float(Text_JSON['lng'])
            count +=1
        elif MIN_Ling > float(Text_JSON['lng']) :
            MIN_Ling = float(Text_JSON['lng'])
    
    return MIN_Ling

        
def PusatLitLng():
    PusatLit = (getMaxLitAll() + getMinLitAll()) / 2
    PusatLng = (getMaxLngAll() + getMinLngAll()) / 2
    return [PusatLit,PusatLng]



def gerLineS():
    ListSinpul = getSimpulAll()
    lisLines = []
    for simpul in ListSinpul:
        listDalam1 =  [float(getLit(simpul)), float(getLng(simpul))]
        for tetangga in getTetangga(simpul):
            ListDalam2 = [float(getLit(tetangga)), float(getLng(tetangga))]
            coba1 = [listDalam1,ListDalam2]
            coba2 = [ListDalam2,listDalam1]
            if coba1 not in lisLines and coba2 not in lisLines:
                lisLines.append(coba1)
    
    return lisLines


#print(gerLineS())