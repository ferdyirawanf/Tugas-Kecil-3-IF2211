import BacaSqlite as BS
import JarakEulidean as JE

def A_Star_Algoritma(NameSimpulAsal, NameSimpulTujuan):
    listKunjungi = []
    ListJawaban = [NameSimpulAsal]
    ListTetangga = BS.getTetangga(NameSimpulAsal)

    while NameSimpulTujuan not in ListJawaban:
        for simpul in ListTetangga:
            ListSimpulJarak = JE.distanceA_Star(ListJawaban[len(ListJawaban)-1,simpul,NameSimpulTujuan])

        #Belum Kelar heheh
