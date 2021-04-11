from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput

from kivy.config import Config




class MyApp(App):

    def build(self):
        button = Button(text='Мой член',
                        font_size=50,
                        on_press = self.button_press,
                        background_normal = '')
        return button

    def button_press(self, instance):
        print('хуй')
        instance.text = 'ТЫ чмо!!'
        instance.background_color = (1, 1, 1, 1)



if __name__ == '__main__':
    MyApp().run()


class dick():
    def suck(self):
        print("suck")

class sperma(dick):
    def chmo(self):
        print('Я гандон')