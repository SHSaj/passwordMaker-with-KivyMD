import hashlib
import pyperclip
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.snackbar import Snackbar

Window.size=(360,640)

KV='''

MDScreen:
    MDTopAppBar:
        title: "Lets Make Password"
        elevation: 2
        pos_hint: {'top': 1}
    MDBoxLayout:
        orientation: 'vertical'
        pos_hint: {'top': 0.9}
        spacing: 20
        MDBoxLayout:
            orientation: 'vertical'
            adaptive_height: True
            padding: 20
            spacing: 10
            MDTextField:
                id: username_field 
                hint_text: "Username"
                mode: "rectangle"
                write_tab: False
            MDTextField:
                id: password_field
                hint_text: "Password"
                password: True
                mode: "rectangle"
                write_tab: False

        MDFillRoundFlatButton:
            text: "     Submit     "
            pos_hint: {'center_x': 0.5}
            on_press: app.press_btn(self)

        MDTabs:
            id: tabs
            tab_hint_x: True
            background_color: app.theme_cls.bg_light
            text_color_normal: 1,1,1,0.8
            text_color_active: app.theme_cls.primary_dark
            indicator_color: app.theme_cls.primary_dark
            Tab:
                title: "16 Digit"
                MDScrollView:
                    MDList:
                        OneLineListItem:
                            id: first_16digit
                            on_release: app.copy_to_clipboard(self.text)
                        OneLineListItem:
                            id: second_16digit
                            on_release: app.copy_to_clipboard(self.text)
                        OneLineListItem:
                            id: third_16digit
                            on_release: app.copy_to_clipboard(self.text)
            Tab:
                title: "12 Digit"
                MDScrollView:
                    MDList:
                        OneLineListItem:
                            id: first_12digit
                            on_release: app.copy_to_clipboard(self.text)
                        OneLineListItem:
                            id: second_12digit
                            on_release: app.copy_to_clipboard(self.text)
                        OneLineListItem:
                            id: third_12digit
                            on_release: app.copy_to_clipboard(self.text)
            Tab:
                title: "8 Digit"
                MDScrollView:
                    MDList:
                        OneLineListItem:
                            id: first_8digit
                            on_release: app.copy_to_clipboard(self.text)
                        OneLineListItem:
                            id: second_8digit
                            on_release: app.copy_to_clipboard(self.text)
                        OneLineListItem:
                            id: third_8digit
                            on_release: app.copy_to_clipboard(self.text)
        
<Tab>
    
'''

class Tab(MDFloatLayout, MDTabsBase):
    pass

class passApp(MDApp):
    def build(self):
        self.theme_cls.material_style = 'M3'
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.theme_style = 'Dark'
        self.Enable = False
        return Builder.load_string(KV)

    def press_btn(self, obj):
        seed = self.root.ids.username_field.text + self.root.ids.password_field.text
        if seed == "":
            Snackbar(text="Please enter a value",
                    duration= 2).open()
        else:
            hashed_string = hashlib.sha512(seed.encode('utf-8')).hexdigest()
            self.root.ids.first_16digit.text = hashed_string[:16]
            self.root.ids.second_16digit.text = hashed_string[16:32]
            self.root.ids.third_16digit.text = hashed_string[32:48]
            self.root.ids.first_12digit.text = hashed_string[:12]
            self.root.ids.second_12digit.text = hashed_string[12:24]
            self.root.ids.third_12digit.text = hashed_string[24:36]
            self.root.ids.first_8digit.text = hashed_string[:8]
            self.root.ids.second_8digit.text = hashed_string[8:16]
            self.root.ids.third_8digit.text = hashed_string[16:24]
            self.Enable = True

    def copy_to_clipboard(self,text):
        if self.Enable:
            pyperclip.copy(text)
            Snackbar(text=f"{text}  Copied to Clipboard!",
                    duration= 2).open()
        else:
            Snackbar(text="Please enter a value",
                    duration= 2).open()

if __name__ == '__main__':
    passApp().run()