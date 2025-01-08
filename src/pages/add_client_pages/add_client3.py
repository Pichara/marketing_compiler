from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class AddClient3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Layout principal
        layout = FloatLayout()

        #Adicionar imagem de fundo
        background = Image(
            source= "assets/images/add_client3.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )
        layout.add_widget(background)

        self.add_widget(layout)