from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class AddClient7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Layout principal
        layout = FloatLayout()

        #Adicionar imagem de fundo
        background = Image(
            source= "assets/images/add_client7.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0}
        )
        layout.add_widget(background)

            #Botão no canto inferior direito
        back_button = Button(
            size_hint=(0.11, 0.2),  #Tamanho do botão
            pos_hint={"x": 0, "y": 0.8},  #Posição no canto inferior direito
            background_color=(0, 0, 0, 0),  #Cor vermelha para destacar
        )
        back_button.bind(on_release=self.show_confirm_popup)
        layout.add_widget(back_button)

        #Buttons para localização entre paginas 
        button_1 = Button(
            size_hint = (0.04, 0.07),
            pos_hint = {"x": 0.32, "y": 0.03},
            background_color = (0,0,0,0),
        )
        
        button_2 = Button(
            size_hint = (0.04, 0.07),
            pos_hint = {"x": 0.36, "y": 0.03},
            background_color = (0,0,0,0),
        )
        
        button_3 = Button(
            size_hint = (0.04, 0.07),
            pos_hint = {"x": 0.4, "y": 0.03},
            background_color = (0,0,0,0),
        )
        
        button_4 = Button(
            size_hint = (0.04, 0.07),
            pos_hint = {"x": 0.44, "y": 0.03},
            background_color = (0,0,0,0),
        )
        
        button_5 = Button(
            size_hint = (0.04, 0.07),
            pos_hint = {"x": 0.48, "y": 0.03},
            background_color = (0,0,0,0),
        )
        
        button_6 = Button(
            size_hint = (0.04, 0.07),
            pos_hint = {"x": 0.52, "y": 0.03},
            background_color = (0,0,0,0),
        )
        
        
        button_8 = Button(
            size_hint = (0.04, 0.07),
            pos_hint = {"x": 0.60, "y": 0.03},
            background_color = (0,0,0,0),
        )
        
        button_9 = Button(
            size_hint = (0.04, 0.07),
            pos_hint = {"x": 0.64, "y": 0.03},
            background_color = (0,0,0,0),
        )
        #Função para mudar de tela
        def change_screen(screen_manager, screen_name, *args):
            screen_manager.current = screen_name

        #Bind para cada botão, associado às páginas no ScreenManager
        button_1.bind(on_release=lambda *args: self.change_screen("add_client_1"))
        button_2.bind(on_release=lambda *args: self.change_screen("add_client_2"))
        button_3.bind(on_release=lambda *args: self.change_screen("add_client_3"))
        button_4.bind(on_release=lambda *args: self.change_screen("add_client_4"))
        button_5.bind(on_release=lambda *args: self.change_screen("add_client_5"))
        button_6.bind(on_release=lambda *args: self.change_screen("add_client_6"))
        button_8.bind(on_release=lambda *args: self.change_screen("add_client_8"))
        button_9.bind(on_release=lambda *args: self.change_screen("add_client_9"))

        layout.add_widget(button_1)
        layout.add_widget(button_2)
        layout.add_widget(button_3)
        layout.add_widget(button_4)
        layout.add_widget(button_5)
        layout.add_widget(button_6)
        layout.add_widget(button_8)
        layout.add_widget(button_9)

        #Botão para a página anterior
        prev_button = Button(
            size_hint=(0.04, 0.07),
            pos_hint={"x": 0.27, "y": 0.03},
            background_color=(0, 0, 0, 0)
        )
        prev_button.bind(on_release=self.go_to_previous_page)
        layout.add_widget(prev_button)

        #Botão para a próxima página
        next_button = Button(
            size_hint=(0.04, 0.07),
            pos_hint={"x": 0.69, "y": 0.03},
            background_color=(0, 0, 0, 0)
        )
        next_button.bind(on_release=self.go_to_next_page)

        layout.add_widget(next_button)
        
        self.add_widget(layout)
        
    def show_confirm_popup(self, instance):
        #Layout do pop-up
        popup_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        #Mensagem de confirmação
        message = Label(text="Tem certeza que deseja voltar à página principal?")

        #Botões do pop-up
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        yes_button = Button(text="Sim", size_hint_x=0.5)
        no_button = Button(text="Não", size_hint_x=0.5)

        #Vinculando ações aos botões
        yes_button.bind(on_release=lambda *args: self.go_to_main(popup))
        no_button.bind(on_release=lambda *args: popup.dismiss())

        #Adiciona os botões ao layout do pop-up
        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        #Adiciona a mensagem e os botões ao layout principal do pop-up
        popup_layout.add_widget(message)
        popup_layout.add_widget(button_layout)

        #Cria o pop-up
        popup = Popup(
            title="Confirmação",
            content=popup_layout,
            size_hint=(0.6, 0.4),
            auto_dismiss=False,
        )
        popup.open()

    def go_to_main(self, popup):
        #Navega para a tela "main_page"
        self.manager.current = "main"

        popup.dismiss()


    def change_screen(self, screen_name, *args):
            self.manager.current = screen_name

    def go_to_previous_page(self, instance):
        current_page = int(self.name.split("_")[-1])
        if current_page > 1:
            self.change_screen(f"add_client_{current_page - 1}")

    def go_to_next_page(self, instance):
        current_page = int(self.name.split("_")[-1])
        if current_page < 9:
            self.change_screen(f"add_client_{current_page + 1}")