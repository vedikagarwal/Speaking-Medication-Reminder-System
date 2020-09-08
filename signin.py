from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from firebase import firebase
firebase = firebase.FirebaseApplication('https://xyzq-3712f.firebaseio.com', None)
result = firebase.get('/s', None)
print (result)
temperature=77
humidity=10
import time
class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        super(SigninWindow, self).__init__(**kwargs)

    def validate_user(self):
        date1 = self.ids.date_field1
        time1 = self.ids.time_field1
        med1 = self.ids.med_field1

        date2 = self.ids.date_field2
        time2 = self.ids.time_field2
        med2 = self.ids.med_field2

        date3 = self.ids.date_field3
        time3 = self.ids.time_field3
        med3 = self.ids.med_field3

        info = self.ids.info

        date1_t = date1.text
        time1_t = time1.text
        med1_t = med1.text

        date2_t = date2.text
        time2_t = time2.text
        med2_t = med2.text

        date3_t = date3.text
        time3_t = time3.text
        med3_t = med3.text

      #  print(passw)
        

        firebase.put('/s', 'date1',date1_t)
        firebase.put('/s', 'time1', time1_t)
        firebase.put('/s', 'med1', med1_t)

        firebase.put('/s', 'date2', date2_t)
        firebase.put('/s', 'time2', time2_t)
        firebase.put('/s', 'med2', med2_t)

        firebase.put('/s', 'date3', date3_t)
        firebase.put('/s', 'time3', time3_t)
        firebase.put('/s', 'med3', med3_t)
        time.sleep(0.01)
        firebase.put('/flag', 'fl', 1)


        print('updated')
        info.text = '[color=#00FF00]updated successfully!!![/color]'

        # if uname == '' or passw == '':
        #     info.text = '[color=#FF0000]username and/ or password required[/color]'
        # else:
        #     if uname == 'admin' and passw == 'admin':
        #         info.text = '[color=#00FF00]Logged In successfully!!![/color]'
        #     else:
        #         info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'


class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__=="__main__":
    sa = SigninApp()
    sa.run()
