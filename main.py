import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text = 'Your Name:'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Fathers Name:'))
        self.f_name = TextInput()
        self.add_widget(self.f_name)

        self.add_widget(Label(text='Mothers Name:'))
        self.m_name = TextInput()
        self.add_widget(self.m_name)

        self.add_widget(Label(text='Gender:'))
        self.gender = TextInput()
        self.add_widget(self.gender)

        self.add_widget(Label(text='NID No:'))
        self.nid = TextInput()
        self.add_widget(self.nid)

        self.add_widget(Label(text='Date of Birth:'))
        self.dob = TextInput()
        self.add_widget(self.dob)

        self.add_widget(Label(text='Your Contact No:'))
        self.conct_no = TextInput()
        self.add_widget(self.conct_no)

        self.add_widget(Label(text='Your E-mail Address is:'))
        self.email_add = TextInput()
        self.add_widget(self.email_add)

        self.add_widget(Label(text='Your Address is:'))
        self.address_info = TextInput()
        self.add_widget(self.address_info)

        self.press = Button(text = 'Click to Submit')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Your Name is: "+self.s_name.text)
        print("Your Father Name is: "+self.f_name.text)
        print("Your Mother Name is: "+self.m_name.text)
        print("Gender is: "+self.gender.text)
        print("Your NID No is: "+self.nid.text)
        print("Your Date of Birth is: "+self.dob.text)
        print("Your Contact No is: "+self.conct_no.text)
        print("Your E-mail Address is: "+self.email_add.text)
        print("Your Address is: "+self.address_info.text)
        print("")


class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()
