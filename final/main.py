from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
#from RPLCD import CharLCD
from RPLCD.gpio import CharLCD
lcd = CharLCD(cols=20, rows=4, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23],numbering_mode=GPIO.BOARD)
from gtts import gTTS
import os
import sqlite3
from sqlite3 import Error
from firebase import firebase
firebase = firebase.FirebaseApplication('https://xyzq-3712f.firebaseio.com', None)
lcd.clear()
sc_date1=[]
firebase.put('/flag', 'fl',1)

###############

entities1=[1]
entities2=[2]
entities3=[3]
def sql_connection():
 
    try:
 
        con = sqlite3.connect('mydatabase.db')
 
        return con
 
    except Error:
 
        print(Error)
        
        
def sql_insert(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO users(id, date, time, medicin) VALUES(?, ?, ?, ?)', entities)
    
    con.commit()        
 
def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE users(id integer PRIMARY KEY, date text, time text, medicin text)")
 
    con.commit()
 
con = sql_connection()
cursorObj = con.cursor()

#############
def fb_get():
    flag_d = firebase.get('/flag', None)
    #print("@@@@@@@@@@@@@@@@@")
    #print(flag_d["fl"])
    if(flag_d["fl"]==1):
        print("works")
    #print("@@@@@@@@@@@@@@@@@")
    
        #result={}
        result = firebase.get('/s', None)
        print result
        col_titles = [k for k in result.keys()]
        #col_titles = [k for k in result.keys()]
        #rows_len = len(result[col_titles[0]])
        print(col_titles)
        print("---------------")
        table_data = []
        sc_date1  *=0
       
        #for t in col_titles:
           # print(t)
        global sc_date1
        sc_date1.append(result["date1"])
        sc_date1.append(result["date2"])
        sc_date1.append(result["date3"])
        
        sc_date1.append(result["time1"])
        sc_date1.append(result["time2"])
        sc_date1.append(result["time3"])
        
        sc_date1.append(result["med1"])
        sc_date1.append(result["med2"])
        sc_date1.append(result["med3"])
        
            #print(sc_date1)
        print(sc_date1)
        firebase.put('/flag', 'fl',0)
        ########
        entities1.append(sc_date1[0])
        entities1.append(sc_date1[3])
        entities1.append(sc_date1[6])
        
        entities2.append(sc_date1[1])
        entities2.append(sc_date1[4])
        entities2.append(sc_date1[7])
        
        entities3.append(sc_date1[2])
        entities3.append(sc_date1[5])
        entities3.append(sc_date1[8])
        
        print("11111111111111")
        print(entities1)
        print(entities2)
        print(entities3)
        print(cursorObj.execute('DELETE FROM users').rowcount)
        sql_insert(con, entities1)
        sql_insert(con, entities2)
        sql_insert(con, entities3)
        print("11111111111111")
        global entities1
        global entities2
        global entities3
        entities1=[1]
        entities2=[2]
        entities3=[3]
        
        
        
#    for r in range(rows_len):
#            for t in col_titles:
#                table_data.append({'text':str(result[0][0])})

def fb_put():
    firebase.put('/s', 'date1','2019/11/19')
    firebase.put('/s', 'time1','02:55:10:am')
    firebase.put('/s', 'med1','hello')
    sleep(0.01)
    firebase.put('/s', 'date2','2019/11/19')
    firebase.put('/s', 'time2','2019/11/19')
    firebase.put('/s', 'med2','hi hi')
    sleep(0.01)
    firebase.put('/s', 'date3','2019/11/19')
    firebase.put('/s', 'time3','2019/11/19')
    firebase.put('/s', 'med3','shiv')
    sleep(0.01)
    firebase.put('/flag', 'fl',3)
    sleep(0.01)

def tts_e(ss):
    tts = gTTS(text=ss, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    
while True:
    currentDT = datetime.now()
    sysc_date1 = currentDT.strftime("%Y/%m/%d")
    sys_time = currentDT.strftime("%I:%M:%P")
    #print(lcd_line_1)
    lcd.cursor_pos = (0, 0) 
    lcd.write_string(sysc_date1)
    lcd.cursor_pos = (1, 0) 
    lcd.write_string(currentDT.strftime("%I:%M:%S:%P"))
    #currentDT = datetime.now()
    #print (currentDT.strftime("%Y-%m-%d %I:%M:%P"))
    #tts_e("hi")
    fb_get()
#    fb_put()
    sleep(0.01)
    #print("///////")
    #print(sc_date1[0])
    #print(sysc_date1)
    #ss=str(sc_date1)
    #ww=str(sysc_date1)
    #print("///////")
    for r in range(3):
        if (sysc_date1==sc_date1[r]) and (sys_time ==sc_date1[r+3]) :
            print("ok")
            lcd.cursor_pos = (2, 0) 
            lcd.write_string(str(sc_date1[r+6]))
            lcd.write_string("         ")
            tts_e(str(sc_date1[r+6]))
            
            
        
            
    #else:
        #print("not ok")
        
