from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class ClientPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Layout principal
        layout = FloatLayout()

        #Adicionar imagem de fundo
        background = Image(
            source= "assets/images/view_client.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )
        layout.add_widget(background)

        self.add_widget(layout)