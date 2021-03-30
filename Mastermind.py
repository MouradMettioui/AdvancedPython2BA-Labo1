import sys
import json
from kivy.app import App
from random import randint
from kivy.config import Config
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.spinner import Spinner
from kivy.graphics import instructions
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class Mastermind(App):
    def build(self):
        self.__manager = ScreenManager()
        self.__manager.add_widget(self.buildScreen1())
        self.__manager.add_widget(self.buildScreen2())
        self.__manager.add_widget(self.buildScreen3())
        return self.__manager

    def buildScreen1(self):
        screen = Screen(name="screen1")
        self.nbr = 0
        self.combinaison = []
        colors =  ['Vert', 'Rose', 'Rouge', 'Bleu', 'Cyan', 'Orange']
        for n in range(0, 4):
            self.combinaison.append(colors[randint(0, 5)])
        self.box = BoxLayout(orientation = "vertical")
        line1 = BoxLayout(orientation = "horizontal")
        ecran1 = Label(text = "Pseudo:", italic = True )
        line1.add_widget(ecran1)
        self.input = TextInput(multiline = False)
        line1.add_widget(self.input)
        self.input.bind(on_text_validate= self._compute)
        ecran2 = Label(text = "BEST:", bold = True )
        line1.add_widget(ecran2)
        self.output = Label()
        line1.add_widget(self.output)
        self.box.add_widget(line1)
        line2 = BoxLayout(orientation = "horizontal")
        self.ecran2bis = Label(text = "essai restant:" + str(10 - self.nbr))
        line2.add_widget(self.ecran2bis) 
        ecran3 = Label(text = "Proposition:", size_hint = (3,1))
        line2.add_widget(ecran3)
        ecran4 = Label(text = "parfait")
        line2.add_widget(ecran4)
        ecran5 = Label(text = "Bonne couleur")
        line2.add_widget(ecran5)
        self.box.add_widget(line2)
        self.lines = BoxLayout(orientation = "vertical", size_hint = (1, 10))
        self.box.add_widget(self.lines)
        self.but = Button(text = "Confirmer")
        self.but.bind(on_press = self.choix)
        lineF = BoxLayout(orientation = "horizontal")
        lineF.add_widget(self.but)
        self.spinner = Spinner(values=('Rouge', 'Vert', 'Bleu', 'Orange', "Rose", "Cyan"))
        lineF.add_widget(self.spinner)
        self.spinner2 =Spinner(values=('Rouge', 'Vert', 'Bleu', 'Orange', "Rose", "Cyan"))
        lineF.add_widget(self.spinner2)
        self.spinner3 = Spinner(values=('Rouge', 'Vert', 'Bleu', 'Orange', "Rose", "Cyan"))
        lineF.add_widget(self.spinner3)
        self.spinner4 = Spinner(values=('Rouge', 'Vert', 'Bleu', 'Orange', "Rose", "Cyan"))
        lineF.add_widget(self.spinner4)
        self.box.add_widget(lineF)
        screen.add_widget(self.box)
        return screen
    
    def _compute(self, source):
        self.phrase = self.input.text
        self.output.text = "{}".format( self.phrase)
    
    def choix(self,source):
        try:
            self.colors = {'Vert':[0, 1, 0, 1], 'Rose':[1, 0, 1, 1], 'Rouge':[1, 0, 0, 1], 'Bleu':[0, 0, 1, 1], 'Cyan':[0, 1, 1, 1], 'Orange':[1, 0.5, 0.3, 1]}
            self. proposition = [self.spinner.text, self.spinner2.text, self.spinner3.text, self.spinner4.text]
            self.ecran = BoxLayout(orientation = "horizontal")
            self.ecran.add_widget(Button(background_color = self.colors[str(self.spinner.text)], size_hint = (1,1)))
            self.ecran.add_widget(Button(background_color = self.colors[str(self.spinner2.text)], size_hint = (1,1)))
            self.ecran.add_widget(Button(background_color = self.colors[str(self.spinner3.text)], size_hint = (1,1)))
            self.ecran.add_widget(Button(background_color = self.colors[str(self.spinner4.text)], size_hint = (1,1)))
            self.lines.add_widget(self.ecran)
            self.nbr +=1
            self.m =0
            self.n=0
            self.ecran2bis.text = "essai restant:" + str(10 - self.nbr)
           
            for i in range(4):
                if self.proposition[i] == self.combinaison[i]:
                    self.m+=1
            for i in set(self.proposition):
                if i in self.combinaison:
                    self.n+=1
            if self.nbr == 10:
                self.__manager.current = "screen3"
            if self.proposition == self.combinaison:
                self.__manager.current = "screen2"
            self.ecran.add_widget(Label(text =str(self.m)))
            self.ecran.add_widget(Label(text=str(self.n)))
        except:
            pass
        
    def buildScreen2(self):
        screen = Screen(name="screen2")
        box = BoxLayout(orientation="vertical")
        box.add_widget(Label(text="GAGNÉ!!!  Vous êtes officiellement maître de votre esprit ;)", size_hint =(1,5), bold = True ))
        self.butt1 = Button(text = "recommencer ?")
        self.butt1.bind(on_press = self.base)
        box.add_widget(self.butt1)
        screen.add_widget(box)
        return screen

    def buildScreen3(self):
        screen = Screen(name="screen3")
        box = BoxLayout(orientation="vertical")
        box.add_widget(Label(text="Perdu... :) la réponse était : " + str(self.combinaison), italic = True))
        self.butt2 = Button(text = "recommencer ?")
        self.butt2.bind(on_press = self.base)
        box.add_widget(self.butt2)
        screen.add_widget(box)
        return screen
    def base(self, source):
        self.__manager.current = "screen1"
        
Mastermind().run()