import pythonfile.BacaSqlite as BS
import pythonfile.JarakEulidean as JE

def A_Star_Algoritma(NameSimpulAsal, NameSimpulTujuan):
    listKunjungi = []
    ListJawaban = [NameSimpulAsal]
    ListTetangga = BS.getTetangga(NameSimpulAsal)
    listResult =[]

    #print(ListTetangga)
    gn = 0
    count = 0
    
    found = False
    while not found:
        
        for simpul in ListTetangga:
            
            ListSimpulJarak = [simpul, gn + JE.distance(BS.getLitLng(ListJawaban[len(ListJawaban)-1]),BS.getLitLng(simpul)) + JE.distance(BS.getLitLng(simpul),BS.getLitLng(NameSimpulTujuan))]
            listKunjungi.append (ListSimpulJarak)
        

        #print(listKunjungi)
        ListMin = []
        for i in range(len(listKunjungi)):
            if i == 0 :
                ListMin = listKunjungi[i]
            elif ListMin[1] > listKunjungi[i][1]:
                ListMin = listKunjungi[i]

        ListJawaban.append(ListMin[0])
        #print("\n",ListMin, "\n")
        listKunjungi.remove(ListMin)
        #print(listKunjungi)

        if ListMin[0] == NameSimpulTujuan:
            found = True
        else:
            # Pencarian gn
            ListTetangga = BS.getTetangga(ListMin[0])
            gn = 0
            CopyList = ListJawaban.copy()
            Back = CopyList.pop()
            ABack = CopyList.pop()
            while ABack not in BS.getTetangga(Back) : ABack = CopyList.pop()

            while  len(CopyList) != 0:
                gn += JE.distance(BS.getLitLng(ABack),BS.getLitLng(Back))
                Back = ABack
                if  len(CopyList) != 0:
                    ABack = CopyList.pop()
                
                


                # for text in ListJawaban:
                #     if text in ListTetangga:
                #         gn += JE.distance(BS.getLitLng(text),BS.getLitLng(Back))
                #         Back = text
                #         ListTetangga = BS.getTetangga(text)
                #         break

            #simpul yang bakal dikunjungi selanjutnya
            ListTetangga = BS.getTetangga(ListMin[0])

        
    gn = 0
    #print(ListJawaban)
    Back = ListJawaban.pop()
    ListTetangga = BS.getTetangga(Back)
    listResult.insert(0,Back)
    while Back != NameSimpulAsal:
        for text in ListJawaban:
            if text in ListTetangga:
                #print(ListTetangga)
                gn += JE.distance(BS.getLitLng(text),BS.getLitLng(Back))
                Back = text
                #print(text)
                listResult.insert(0,Back)
                ListTetangga = BS.getTetangga(text)
                break
   
    listReturn = [listResult, gn]
    count = 0
    Hasil =""
    for text in listReturn[0]:
        if count == len(listReturn[0]) -1:
            Hasil += text + ".\nJarak : " + str(listReturn[1]) + " KM"
        else:
            Hasil += text + " ---> "
        count +=1

    #print(Hasil)
    listReturn.append(Hasil)
    return listReturn

def getLitLngHasil(NameSimpulAsal, NameSimpulTujuan):
    ListHasil = A_Star_Algoritma(NameSimpulAsal, NameSimpulTujuan)[0]
    print("\nRekomendasi Jalur:\n" + A_Star_Algoritma(NameSimpulAsal, NameSimpulTujuan)[2],"\n")
    listLitLngHasil =[]
    for text in ListHasil:
        listLitLngHasil.append([float(BS.getLit(text)), float(BS.getLng(text))])
    return listLitLngHasil


#print(getLitLngHasil("Pintu Utama ITB","Simpang Departemen Fisika"))        
#print(A_Star_Algoritma("B1","G1"))           
