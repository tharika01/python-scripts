import tkinter
from tokenize import Number
import tkintermapview
import phonenumbers

#from key import key
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

from tkinter import *
from tkinter import messagebox
from opencage.geocoder import OpenCageGeocode


root = tkinter.Tk()
root.geometry("500x500")

label1=Label(text="MOBILE PHONE TRACKER")
label1.pack()

import requests

key = "48dc4626c36b4f13bcf53c3111f082a4"
response = requests.get("http://api.ipstack.com/134.201.250.155?access_key=9ec7914b61611abd1ab55bb636157214")
print(response.status_code)
print(response.content)

def getResult():
    num = number.get("1.0",END)
    num1=phonenumbers.parse(num)
    gb_number=phonenumbers.parse(num,"GB")
    
    location=geocoder.description_for_number(num1,"en")
    service_provider = carrier.name_for_valid_number(num1,"en")
    Time_zone_desc=timezone.time_zones_for_geographical_number(gb_number) 
    print(str(location))
    ocg = OpenCageGeocode(key)
    query = str("Bangalore, Karnataka")
    results=ocg.geocode(query)
    
    lat=results[0]['geometry']['lat']
    lng=results[0]['geometry']['lng']
    
    my_label=LabelFrame(root)
    my_label.pack(pady=20)
    
    map_widget= tkintermapview.TkinterMapView(my_label,width=450,height=450,corner_radius=0)
    
    map_widget.set_position(lat,lng)
    map_widget.set_marker(lat,lng,text="Phone location")
    map_widget.set_zoom(10)
    map_widget.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    map_widget.pack()
    
    adr = tkintermapview.convert_coordinates_to_address(lat, lng)

    result.insert(END,"The country of this number is:"+location)
    result.insert(END,"\nThe  sim card of this number is:" + service_provider)
    
    
    result.insert(END,"\nLatitude is: "+str(lat))
    result.insert(END,"\nLongitude is: "+str(lng))
    
    #result.insert(END,"\nTime zone is: "+str(Time_zone_desc))

    result.insert(END, "\nStreet Address is :" +adr.street)
    result.insert(END, "\nCity Address is :" +adr.city)
    result.insert(END, "\nPostal Code is :" +adr.postal)
    
number=Text(height=1)
number.pack()

button = Button(text="Search",command=getResult)
button.pack(pady=10,padx=100)

result=Text(height=7)
result.pack()

root.mainloop()