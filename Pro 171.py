from tkinter import *
from PIL import ImageTk , Image
from datetime import datetime
import pytz 
import time

root = Tk()
root.title("Time")
root.geometry("1000x1000")

ind_img = ImageTk.PhotoImage(Image.open("india.jpg"))
usa_img = ImageTk.PhotoImage(Image.open("usa.jpg"))
japan_img = ImageTk.PhotoImage(Image.open("japan.jpg"))
australia_img = ImageTk.PhotoImage(Image.open("australia.jpg"))

india_label = Label(root , text = "India")
india_label.place(relx=0.3 , rely=0.1 , anchor=CENTER)

india_pm = Label(root)
india_pm["image"] = ind_img
india_pm.place(relx=0.3 , rely=0.2 , anchor=CENTER)

india_time = Label(root)
india_time.place(relx=0.3 , rely=0.3 , anchor=CENTER)
#
usa_label = Label(root , text = "USA")
usa_label.place(relx=0.7 , rely=0.1 , anchor=CENTER)

usa_pm = Label(root)
usa_pm["image"] = usa_img
usa_pm.place(relx=0.7 , rely=0.2 , anchor=CENTER)

usa_time = Label(root)
usa_time.place(relx=0.7 , rely=0.3 , anchor=CENTER)

#
japan_label = Label(root , text = "Japan")
japan_label.place(relx=0.3 , rely=0.6 , anchor=CENTER)

japan_pm = Label(root)
japan_pm["image"] = japan_img
japan_pm.place(relx=0.3 , rely=0.7, anchor=CENTER)

japan_time = Label(root)
japan_time.place(relx=0.3 , rely=0.8 , anchor=CENTER)

#
australia_label = Label(root , text = "Australia")
australia_label.place(relx=0.7 , rely=0.6 , anchor=CENTER)

australia_pm = Label(root)
australia_pm["image"] = australia_img
australia_pm.place(relx=0.7 , rely=0.7 , anchor=CENTER)

australia_time = Label(root)
australia_time.place(relx=0.7 , rely=0.8 , anchor=CENTER)

class India():
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        india_time["text"] = "Time : " + current_time
        india_time.after(200 , self.times)
 
class US():
    def times(self):
        home = pytz.timezone("US/Central")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        usa_time["text"] = "Time : " + current_time
        usa_time.after(200 , self.times)        
 
class Aus():
    def times(self):
        home = pytz.timezone("Australia/ACT")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        australia_time["text"] = "Time : " + current_time
        australia_time.after(200 , self.times)    
        
class Japan():
    def times(self):
        home = pytz.timezone("Japan")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H : %M : %S")
        japan_time["text"] = "Time : " + current_time
        japan_time.after(200 , self.times)        
         
obj_india = India()
obj_usa = US()
obj_australia = Aus()
obj_japan = Japan()

        

btn_ind = Button(root , text="Show Time", command=obj_india.times )
btn_ind.place(relx=0.3 , rely=0.4 , anchor=CENTER)

btn_usa = Button(root , text="Show Time", command = obj_usa.times )
btn_usa.place(relx=0.6 , rely=0.4 , anchor=CENTER)

btn_japan = Button(root , text="Show Time", command = obj_japan.times )
btn_japan.place(relx=0.3 , rely=0.9 , anchor=CENTER)

btn_aus = Button(root , text="Show Time", command = obj_australia.times )
btn_aus.place(relx=0.6 , rely=0.9 , anchor=CENTER)




root.mainloop()