from kivy.config import Config

# Set configurations for the Kivy window before everything
Config.set('kivy', 'window_icon', 'images/icones/VidaVivaIcon.png')  # Define o ícone da janela
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')  # Configurações de input do mouse
Config.set('graphics', 'width', '1300')  # Largura da janela
Config.set('graphics', 'height', '700')  # Altura da janela
Config.set('graphics', 'resizable', '0')  # Desabilita redimensionamento
Config.set('graphics', 'borderless', '0')  # Ativa bordas da janela

#Import of all the pages
from pages.main_page import MainPage
from pages.client_page import ClientPage
from pages.add_client_pages.add_client1 import AddClient1
from pages.add_client_pages.add_client2 import AddClient2
from pages.add_client_pages.add_client3 import AddClient3
from pages.add_client_pages.add_client4 import AddClient4
from pages.add_client_pages.add_client5 import AddClient5
from pages.add_client_pages.add_client6 import AddClient6
from pages.add_client_pages.add_client7 import AddClient7
from pages.add_client_pages.add_client8 import AddClient8
from pages.add_client_pages.add_client9 import AddClient9

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

#Main App class with ScreenManager
class MyApp(App):
    def build(self):
        # Initialize ScreenManager
        sm = ScreenManager()

        #All the pages
        sm.add_widget(MainPage(name="main"))
        sm.add_widget(ClientPage(name="client"))
        sm.add_widget(AddClient1(name="add_client_1"))
        sm.add_widget(AddClient2(name="add_client_2"))
        sm.add_widget(AddClient3(name="add_client_3"))
        sm.add_widget(AddClient4(name="add_client_4"))
        sm.add_widget(AddClient5(name="add_client_5"))
        sm.add_widget(AddClient6(name="add_client_6"))
        sm.add_widget(AddClient7(name="add_client_7"))
        sm.add_widget(AddClient8(name="add_client_8"))
        sm.add_widget(AddClient9(name="add_client_9"))

        return sm

#Run the app
if __name__ == '__main__':
    MyApp().run()
