
import folium



map = folium.Map(location=[53.3498, -6.2603],
              zoom_start=15)

loc = [(53.3498, -6.2603),
       (53.2669, -6.1840)]

folium.PolyLine(loc,
                color='red',
                weight=10,
                opacity=0.8).add_to(map)
map.save('map3.html')