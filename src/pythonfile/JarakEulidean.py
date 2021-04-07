import math
#import BacaSqlite as BS

def distance(litlng1, litlng2):
    # Menembalikan jaran ataran 2 simpul garis lurus
    val1 =  (float(litlng1[0]) - float(litlng2[0]))**2
    val2 = (float(litlng1[1]) - float(litlng2[1]))**2
    return math.sqrt( val1 + val2)

def distanceA_Star (litlng_asal,litlng_tetangga, litlng_tujuan):
    # mengembalikan perhitungan jarak distanceA_Star 
    distance_1 = distance(litlng_asal,litlng_tetangga)
    distance_2 = distance(litlng_asal,litlng_tujuan)
    return distance_1 + distance_2

#print(distance(BS.getLitLng("Pintu Utama ITB") ,BS.getLitLng("Simpang Aula Barat") ) )