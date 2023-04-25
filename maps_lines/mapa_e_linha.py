from functools import partial
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivymd.app import MDApp
from kivy_garden.mapview import MapView, MapMarker

class MapViewApp(MDApp):
    def build(self):
        mapData = MapView(zoom=6, lat=10.4735, lon=55.9754)
        marker1 = MapMarker(lat=20.3572136, lon=43.5032709)
        marker2 = MapMarker(lat=20.3572136, lon=53.5032709)
        mapData.add_marker(marker1)
        mapData.add_marker(marker2)
        self.line = None
        mapData.bind(on_map_relocated=partial(self.draw_line, marker1, marker2))
        return mapData

    def draw_line(self, m1, m2, *args):
        if self.line is None:
            with self.root.canvas:
                Color(1, 0, 0, 1)
                self.line = Line(points=[m1.center_x, m1.y, m2.center_x, m2.y], width=1)
        else:
            self.line.points = [m1.center_x, m1.y, m2.center_x, m2.y]

if __name__ == "__main__":
    MapViewApp().run()