import math
from math import sin, cos, sqrt, atan2, radians

R = 6373.0

def distance(litlng1, litlng2):
    # Menembalikan jaran ataran 2 simpul garis lurus
    val1 =  (radians(float(litlng1[0])) - radians(float(litlng2[0])))**2
    val2 = (radians(float(litlng1[1])) - radians(float(litlng2[1])))**2
    a = (sin(val1/2))**2 + cos(radians(float(litlng1[0]))) * cos(radians(float(litlng2[0]))) * (sin(val2/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def distanceA_Star (litlng_asal,litlng_tetangga, litlng_tujuan):
    # mengembalikan perhitungan jarak distanceA_Star 
    distance_1 = distance(litlng_asal,litlng_tetangga)
    distance_2 = distance(litlng_asal,litlng_tujuan)
    return distance_1 + distance_2

#print(distance(BS.getLitLng("Pintu Utama ITB") ,BS.getLitLng("Simpang Aula Barat") ) )