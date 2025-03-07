import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class ChildApp(GridLayout):
    def __init__ (self, ** kw_args):
     super(ChildApp,self).__init__()
     self.cols = 2

     self.add_widget (Label(text = 'student name'))
     self.s_name = TextInput()
     self.add_widget (self.s_name)

     self.add_widget (Label(text = 'student marks'))
     self.s_marks = TextInput()
     self.add_widget (self.s_marks)

     self.add_widget (Label(text = 'student gender'))
     self.s_gender = TextInput()
     self.add_widget (self.s_gender)

     self.press=Button(text = 'click me')
     self.press.bind(on_press=self.click_me)
     self.add_widget(self.press)

    def click_me(self , instance):
        print("Name of student is " + self.s_name.text)
        print("Mark of student is " + self.s_marks.text)
        print("Gender of student is " + self.s_gender.text)
        print("")

class parentApp(App):
    def build(self):
        return ChildApp()

if __name__=="__main__":
    parentApp().run()
