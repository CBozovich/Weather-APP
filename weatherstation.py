from tkinter import *
import requests
import json

root = Tk()
root.title("Bozovich Weather")
root.geometry("325x200")

#zip looup
def zipLookup():
    #zip.get()
    #zipLable = Label(root, text= zip.get())
    #zipLable

    try:
        api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + zip.get() +"&units=imperial&appid=cf33aa6d75c03f65454938445632daba").json()

        city = api_request["name"]
        temp = api_request['main']['temp']
        high = api_request['main']['temp_max']
        low = api_request['main']['temp_min']
        feel = api_request['main']['feels_like']

        # City and current temp
        myLabel = Label(root, text= city + " " + str(temp))
        myLabel.grid(row=3, column=1, columnspan=2)

        # feels like temp
        myLabel_2 = Label(root, text= (" Feels Like ") + " " + str(feel))
        myLabel_2.grid(row=9, column=1, columnspan=2)

        # High Temp
        myLabel_3 = Label(root, text = " Todays High " + " " + str(high))
        myLabel_3.grid(row=5, column=1, columnspan=3)

        # Low Temp
        myLabel_4 = Label(root, text = " Todays Low " + " " + str(low))
        myLabel_4.grid(row=7, column=1, columnspan=2)

    except Exception as e:
        api = " ERROR... "


# Zip Code Lookup
zip = Entry(root)
zip.grid(row= 0, column= 1, padx= 5, pady= 10)

zipButton = Button(root, text= "Zip Code Search", command=zipLookup)
zipButton.grid(row=1, column=1, padx=95, pady=10)

# Units of weather
#units = StringVar(value)

#Radiobutton(root, text=" F ", variable=units, value=" imperial ", command=sel).grid(row=0, column=0)
#Radiobutton(root, text=" C ", variable=units, value=" metric ", command=sel)R2.grid(row=1, column=0)

#radioLable = Entry(root)
#radioLable.grid(row=1, column=0)

root.mainloop()