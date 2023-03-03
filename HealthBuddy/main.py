from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty
from kivy.metrics import dp  # FOR SIZE
import os



from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


from navigation_screen_manager import NavigationScreenManager

# from kivy.uix.BoxLayout import BoxLayout


# kv=Builder.load_file('login.kv')
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass

class MyScreenManager(NavigationScreenManager):
    pass


kv = Builder.load_file('main.kv')

class MainApp(App):
    profile = {
        "user": " ",
        "pass": " ",
        "sex": " ",
        "activ": " ",
        "ideal": " ",
        "zona": " ",
        "apa": " ",
        "calorii": " ",
        "apabauta": "0",
        "caloriicons": "0"
    }

    manager = ObjectProperty(None)
    manager = MyScreenManager()
    # when you build you return your main interface
    def build(self):
        return kv

    # when you build you return your main interface

    #Alexa Functii:

    def clear(self,widget):
        widget.ids.welcome_label.text='WELCOME'
        widget.ids.user.text=''
        widget.ids.password.text=''

    def salut(self, widget):
        widget.ids.otp_label.text = "Buna, " + self.profile['user'] + "!!!"
        if self.profile["apa"] == " ":
            self.profile["apa"] = '0'
        widget.ids.water_label.text = "Astazi ai baut: " + str(self.profile["apabauta"]) + " ml!"
        if self.profile["calorii"] == " ":
            self.profile["calorii"] = '0'
        widget.ids.cal_label.text = "Astazi ai consumat: " + str(self.profile["caloriicons"]) + " kcal!"
        
    #Diana Functii:

    def checkbox_click(self, widget, var):

            widget.ids.output_label.text = f'Ati Modificat : {var}'

    def checkbox_radio(self, widget, nume, checkbox, state):
        print("checkbox changed state")

        if nume in { "F", "M", "Na" }:
            self.profile["sex"] = nume
            for x in range(0, 3):
                if widget.children[0].children[10].children[2 * x].name != nume:
                    widget.children[0].children[10].children[2 * x].active = False


        if nume in {"medie", "intensa", "foarte intensa", "sedentar"}:
            self.profile["activ"] = nume
            for x in range(0, 4):
                if widget.children[0].children[7].children[2 * x].name != nume:
                    widget.children[0].children[7].children[2 * x].active = False

        if nume in {"Slabit", "greutate", "Mentinere"}:
            self.profile["ideal"] = nume
            for x in range(0, 3):
                if widget.children[0].children[4].children[2 * x].name != nume:
                    widget.children[0].children[4].children[2 * x].active = False

        if nume in {"sus", "jos", "Cardio", "Intreg"}:
            self.profile["zona"] = nume
            for x in range(0, 4):
                if widget.children[0].children[1].children[2*x].name != nume:
                    widget.children[0].children[1].children[2*x].active = False



    #Mihaela functii:
    
    def functie(self,m, a, h,s):  # functie care calculeaza cata APA trebuie o persoana sa bea MINIM pe zi, in functie de masa, inaltime si sex, dar si cate calorii trb sa consume pe zi

        apa = str((m * 5.4) + 2000) + " ml"
        if s == "M":
            RMB = 66 + 13.7 * m + 5 * h - 6.8 * a
        elif s == "F":
            RMB = 655 + 9.5 * m + 1.8 * h - 4.7 * a
        else:
            RMB = 0

        calori = str(round((RMB * 1.55),2)) + " cal"
        calori_s = str(round(((RMB * 1.55) - 200)*0.9,2)) + " cal" # calorii pt slabit
        calori_i = str(round(((RMB * 1.55) + 200)*1.2,2)) + " cal" # calorii pt ingrasat

        return {'apa': apa, 'calorii': calori, 'calorii_s': calori_s, 'calorii_i': calori_i}

    def calculate(self,widget):
        try:
            masa = int(widget.greutate.text)
            age = int(widget.varsta.text)
            height = int(widget.inaltime.text)
            sex = self.profile["sex"]

        except:
            masa = 0
            age = 0
            height = 0
            sex = "null"

        persoana = self.functie(masa, age, height, sex)

        widget.apa.text = persoana.get('apa')
        self.profile["apa"] = persoana.get('apa')
        widget.calorii.text = persoana.get('calorii')
        self.profile["calorii"] = persoana.get('calorii')
        widget.calorii_s.text = persoana.get('calorii_s')
        widget.calorii_i.text = persoana.get('calorii_i')

    # Maria functii
    def press_water(self, widget):
        str = self.profile["apa"]
        str = str[:-3]

        water = float(str)

        water_add = float(widget.ids.water_input.text)

        widget.ids.water_label.text = "Ai adaugat " + widget.ids.water_input.text + " de ml de apa!"

        current = widget.ids.water_progres.value

        current += float(water_add / water)
        
        widget.ids.water_progres.value = current

        str2 = self.profile["apabauta"]
        str2 = float(str2) + float(widget.ids.water_input.text)
        
        self.profile["apabauta"] = str2



    def press_calorie(self, widget):
        str = self.profile["calorii"]
        str = str[:-5]

        calorie = float(str)

        calorie_add = float(widget.ids.calorie_input.text)

        widget.ids.calorie_label.text = "Ai adaugat " + widget.ids.calorie_input.text + " kcal!"

        current = widget.ids.calorie_progres.value

        current += float(calorie_add / calorie)

        widget.ids.calorie_progres.value = current
        
        str2 = self.profile["caloriicons"]
        str2 = float(str2) + float(widget.ids.calorie_input.text)

        self.profile["caloriicons"] = str2


    def on_text_validate(self, text):
        self.profile.user = text
        print(self.profile.user)
    def print_profile(self):
        print(self.profile)

    def on_password_validate(self, data):
        self.profile["pass"] = str(data)

    def on_user_validate(self, data):
        self.profile["user"] = str(data)

MainApp().run()