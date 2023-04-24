from kivy_garden.mapview import geojson
from kivy.app import App


class AppTitle(App):
    def __init__(self, **kwargs):
        super(AppTitle, self).__init__(**kwargs)
        


def main():
    AppTitle().run()


if __name__ == '__main__':
    main()
