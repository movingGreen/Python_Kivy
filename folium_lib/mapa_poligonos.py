# import folium library
import folium

# create a map object
mapObj = folium.Map(location=[22.64443248121717, 79.80468750000001],
                    zoom_start=6)

# create a layer on the map object
shapesLayer = folium.FeatureGroup(name="Vector Shapes").add_to(mapObj)

# create a rectangle object and add to map
folium.Rectangle(
    [(28.0214793, 73.2845211), (22.7241158, 75.7938099)],
    weight=2,
    fill_color="orange",
    fill_opacity=0.4).add_to(shapesLayer)

# create a polyline with the coordinates
folium.PolyLine([(28.5274851, 77.1389452), (27.1763098, 77.9099731), (23.199552, 77.3358515),
                 (21.1612315, 79.0024702), (17.661548, 75.8835978)],
                color="green",
                weight=4).add_to(shapesLayer)

# create a polygon with the coordinates
folium.Polygon([(25.4024022, 81.7315446), (25.6081756, 85.073003), (20.4631843, 85.8327264),
                (19.0860155, 82.0161332), (21.4692684, 80.1817197)],
               weight=2,
               color="red",
               fill_color="yellow",
               fill_opacity=0.3).add_to(shapesLayer)

# create a circle
folium.CircleMarker(location=[23.294059708387206, 78.26660156250001],
              radius=50
              ).add_to(shapesLayer)


# display the layer switcher widget
folium.LayerControl().add_to(mapObj)

# save the map object as a html
mapObj.save('output.html')