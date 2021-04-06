import sqlite3
import json

def FiletoSql(filename):
    #mempersiapkan tempat sqlite
    path = "../sqlite/"
    conn = sqlite3.connect(path+'DataGeoLoad.sqlite3')
    cur = conn.cursor()

    cur.executescript("""
    DROP TABLE IF EXISTS Locations;

    CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)
    """)

    #membuka file
    fileisOpen = open(filename)
    isiFile = fileisOpen.readlines()
    Ndata = 0
    listGeo = list()
    listMatrik = list()
    daftarGraf = list()
    count = 0
    for text in isiFile:
        if count == 0 : Ndata =  int(text)
        elif count <= Ndata: 
            text = text.replace('\n','')
            listGeo.append(text)
        elif count <= 2*Ndata:
            text = text.replace('\n','')
            listMatrik.append(text)
        count += 1
    

    for i in range(Ndata):
        text1 = listGeo[i].split(" ")
        NamePlace = ""
        count = len(text1)
        for i in range(count):
            if i == count -1 : NamePlace += text1[i]
            elif i != 0 and i !=1: NamePlace += text1[i] + " "
        daftarGraf.append(NamePlace)
        


    for i in range(Ndata):
        text1 = listGeo[i].split(" ")
        text2 = listMatrik[i].split(" ")
        lit = text1[0]
        ling = text1[1]
        #print(daftarGraf[i])
        listGrafTetangga = list()
        count = 0
        for text in text2 :
            if text == "1":
                listGrafTetangga.append(daftarGraf[count])
            count += 1
        
        #print(listGrafTetangga)
        isiDict = {}
        isiDict.update({"lit":lit})
        isiDict.update({"lng":ling})
        isiDict.update({"tetangga": listGrafTetangga})
        #print(isiDict)

        cur.execute('''INSERT INTO Locations (address, geodata) VALUES ( ?, ? )''', (str(daftarGraf[i]), json.dumps(isiDict)))
        conn.commit()




     


#FiletoSql("../../test/itb_depan.txt")





