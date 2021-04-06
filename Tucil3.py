from math import radians, cos, sin, asin, sqrt

def input_file():
    data = []
    file = open("coba.txt", "r")
    for i in file:
        i = i.replace("\n", "")
        data.append(i.split(", "))
    return data

def simpul(input_list,n):
    list_simpul = []
    for i in range(1,len(input_list)-n):
        list_simpul += [input_list[i][0]]
    return list_simpul

def lat(input_list,n):
    list_latitude = []
    for i in range(1,len(input_list)-n):
        list_latitude += [float(input_list[i][1])]
    return list_latitude

def lon(input_list,n):
    list_longitude = []
    for i in range(1,len(input_list)-n):
        list_longitude += [float(input_list[i][2])]
    return list_longitude

def matriks(input_list,n):
    matriks_adj = []
    for i in range(n+1, len(input_list)):
        kolom = []
        for j in range(len(input_list[i])):
            kolom += [float(input_list[i][j])]
        matriks_adj += [kolom]
    return matriks_adj

def ubahMatriks(matriksAdj, mlat, mlon):
    for i in range(len(matriksAdj)):
        for j in range(len(matriksAdj[i])):
            if (matriksAdj[i][j]) != 0.0:
                matriksAdj[i][j] = haversine(mlat[i], mlon[i], mlat[j], mlon[j])
    return matriksAdj

def cari_simpul(simpul, list_simpul):
    i = 0
    temu = False
    while i < len(list_simpul) and temu == False:
        if list_simpul[i] == simpul:
            temu = True
        i = i+1
    return i-1

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

n = int(input_file()[0][0])
simpul = simpul(input_file(),n)
list_lat = lat(input_file(),n)
list_lon = lon(input_file(),n)
matriksadj = matriks(input_file(),n)
matriksadjj = ubahMatriks(matriksadj, list_lat, list_lon)
asal = input("Masukkan simpul asal: ")
tujuan = input("Masukkan simpul tujuan: ")
idx_asal = cari_simpul(asal,simpul)
idx_tujuan = cari_simpul(tujuan,simpul)

hasil = [0.0, simpul[idx_asal]]
while idx_asal != idx_tujuan:
    list_hn = []
    for i in range(len(matriksadjj)):
        lhn_kol = []
        if matriksadjj[idx_asal][i] != 0.0:
            gn = matriksadjj[idx_asal][i] + hasil[0]
            hn = haversine(list_lat[i], list_lon[i], list_lat[idx_tujuan], list_lon[idx_tujuan])
            fn = gn+hn
            lhn_kol += [fn]
            lhn_kol += [i]
            list_hn += [lhn_kol]

    min = list_hn[0]
    for i in range(len(list_hn)):
        if min[0] > list_hn[i][0]:
            min  = list_hn[i]

    hasil[0] += matriksadjj[idx_asal][min[1]]
    hasil += [simpul[min[1]]]
    idx_asal = min[1]

print(hasil)