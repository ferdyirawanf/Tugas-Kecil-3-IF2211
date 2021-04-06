import folium
from folium import IFrame
import os
import base64
import BacaSqlite as BS

ListSinpul = BS.getSimpulAll()
cob1 = BS.gerLineS()
m = folium.Map(location= BS.PusatLitLng(), zoom_start = 17)
for text in cob1:
    folium.PolyLine(text).add_to(m)

for text in ListSinpul:
    folium.Marker(location = BS.getLitLng(text)).add_to(m)

m.save("index.html")
