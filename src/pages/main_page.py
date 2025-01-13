from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout


class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Layout principal
        layout = FloatLayout()

        #Adicionar imagem de fundo
        background = Image(
            source= "assets/images/main_page.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )
        layout.add_widget(background)

        #TextInput para pesquisa
        search_box = TextInput(
            hint_text="Pesquisar...",
            size_hint=(0.13, 0.06),
            pos_hint={'x': 0.78, 'y': 0.750}  #Posicionando na área do ícone de lupa
        )
        search_box.bind(text=self.filter_clients)
        layout.add_widget(search_box)

        #Botão invisível para "Adicionar Cliente"
        add_client_btn = Button(
            size_hint=(0.17, 0.1),
            pos_hint={'x': 0.12, 'y': 0.74},
            background_color=(0, 0, 0, 0)  #Totalmente invisível
        )
        add_client_btn.bind(on_release=self.go_to_add_client)
        layout.add_widget(add_client_btn)

        #ScrollView para exibir a lista de clientes
        self.client_list_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.client_list_layout.bind(minimum_height=self.client_list_layout.setter('height'))

        #Adicionar clientes de exemplo (isso será substituído pela conexão com Firebase)
        for i in range(20):
            client_label = Label(
                text=f"Cliente {i + 1}",
                size_hint_y=None,
                height=40
            )
            self.client_list_layout.add_widget(client_label)

        scroll_view = ScrollView(size_hint=(0.761, 0.68), pos_hint={'x': 0.118, 'y': 0})
        scroll_view.add_widget(self.client_list_layout)
        layout.add_widget(scroll_view)

        self.add_widget(layout)

    def go_to_add_client(self, instance):
        #Redireciona para a página "add_client_1"
        self.manager.current = "add_client_1"

    def filter_clients(self, instance, text):
        #Filtra a lista de clientes com base no texto digitado
        for widget in self.client_list_layout.children:
            if isinstance(widget, Label):
                widget.opacity = 1 if text.lower() in widget.text.lower() else 0
                widget.disabled = False if text.lower() in widget.text.lower() else True
