import folium
from folium import IFrame
import os
import base64
import pythonfile.BacaSqlite as BS
import pythonfile.TucilAstar as TA

def ExportHTML(NameSimpulAsal, NameSimpulTujuan):
    ListSinpul = BS.getSimpulAll()
    cob1 = BS.gerLineS()
    cob2 = TA.getLitLngHasil(NameSimpulAsal,NameSimpulTujuan)
    listHasil_jarak = TA.A_Star_Algoritma(NameSimpulAsal,NameSimpulTujuan)
    m = folium.Map(location= BS.PusatLitLng(), zoom_start = 17)
    for text in cob1:
        folium.PolyLine(text).add_to(m)


    folium.PolyLine(cob2, color='orange').add_to(m)

    count = 0
    for text in listHasil_jarak[0]:
        if count == 0 :
            folium.Marker(location = BS.getLitLng(text),popup= text, icon=folium.Icon(color="green")).add_to(m)
        elif count == len(listHasil_jarak[0]) -1:
            folium.Marker(location = BS.getLitLng(text),popup= text, icon=folium.Icon(color="red")).add_to(m)
        else:
            folium.Marker(location = BS.getLitLng(text),popup= text, icon=folium.Icon(color="orange")).add_to(m)
        count += 1


    for text in ListSinpul:
        if text in listHasil_jarak[0]: continue
        folium.Marker(location = BS.getLitLng(text), popup= text, icon=folium.Icon(color="blue")).add_to(m)






    #m.add_child(folium.LatLngPopup())
    m.save("index.html")


