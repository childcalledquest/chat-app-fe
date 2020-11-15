import kivy

from kivy.app import App
from kivy.uix.label import label

class Main(App):

    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    Main.run()

